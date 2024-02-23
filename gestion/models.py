from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Plato(models.Model):
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)
    # width_field y height_field sirven para poder indicar las dimensiones de la imagen pero estas dimensiones seran utilizadas si es que vamos a utilizar las templates de django
    foto = models.ImageField()

    class Meta:
        # https://docs.djangoproject.com/en/5.0/ref/models/options/
        # sirve para indicar como se llamara la tabla en la base de datos
        db_table = 'platos'


class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descripcion = models.TextField(null=False)
    # para crear una relacion entre dos modelos se usa el ForeignKey
    # to > sirve para indicar la referencia hacia la tabla con la cual crearemos la relacion
    # db_column > indicar como se va a llamar esta columna en la base de datos
    # on_delete > indicar como se va a comportar cuando se elimine el padre (Plato al cual pertenece)
    # CASCADE > si se elimina el plato, se eliminaran todos sus ingredientes
    # PROTECT > evita la eliminacion del plato si tiene ingredientes lanzado un error de tipo ProtectedError
    # RESTRICT > evita la eliminacion del plato si tiene ingredientes y lanza un error de tipo RestrictedError
    # SET_NULL > permite la eliminacion del plato y le cambia el valor a sus ingredientes a la columna plato_id a NULL (los deja huerfanos)
    # SET_DEFAULT > permite la eliminacion del plato y cambia el valor de la columna a un valor por defecto
    # DO_NOTHING > permite la eliminacion del plato y no cambia el valor del ingrediente del plato_id generando inconsistencia de datos
    # related_name > funciona muy similar al relationships de flask y eso significa que creara un atributo virtual en el modelo en el cual estemos creando la conexion, en este caso en el modelo PLATO
    platoId = models.ForeignKey(
        to=Plato, db_column='plato_id', on_delete=models.PROTECT, related_name='ingredientes')

    class Meta:
        db_table = 'ingredientes'


class Preparacion(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descripcion = models.TextField(null=False)
    orden = models.IntegerField(null=False)
    platoId = models.ForeignKey(
        to=Plato, db_column='plato_id', on_delete=models.PROTECT, related_name='preparaciones')

    class Meta:
        db_table = 'preparaciones'
        # indicar cual sera el ordenamiento al momento de hacer un select
        # ['orden'] > indicar que ahora el ordenamiento sera en relacion al orden de manera ascendente
        # ['-orden'] > indicar que el ordenamiento sera de manera DESCENDENTE
        # el ordering no se da a nivel de base de datos, solamente a nivel del backend
        ordering = ['-orden']
        # el orden y el plato al cual pertenece esta preparacion jamas se puede repetir
        # unique_together si se da a nivel de base de datos (se crea la contraint UNIQUE en la base de datos)
        unique_together = [['orden', 'platoId']]


# vamos a utilizar el modelo auth_user proveniente del panel administrativo
class Cheff(AbstractBaseUser):
    # permite modificar por completo mi tabla auth_user de django
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)
    # EmailField > a parte de guardar como un texto en la base de datos añade validacion para que el texto ingresado sea un correo
    correo = models.EmailField(unique=True, null=False)
    # si vamos a configurar la password si o si tiene que llamarse password
    password = models.TextField(null=False)

    # para que siga funcionando el panel administrativo de django tenemos que configurar las siguientes columnas
    # is_staff > sirve para indicar que el usuario que estamos creando puede tener acceso al panel administrativo
    is_staff = models.BooleanField(default=False)
    # is_active > sirve para indicar si el usuario tiene acceso o no al panel administrativo y este se puede cambiar si, por ejemplo el usuario deja de estar activo en la aplicacion
    is_active = models.BooleanField(default=True)

    # para poder realizar el login en el panel administrativo tenemos que definir que columna se usara como username
    USERNAME_FIELD = 'correo'
    # sirve para pedirle al usuario al momento de crear un superusuario por la consola
    # python manage.py createsuperuser
    # no se debe declarar el atributo del username_field ni los campos password
    REQUIRED_FIELDS = ['nombre']

    class Meta:
        db_table = 'cheffs'
