from django.db import models


class Plato(models.Model):
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)

    class Meta:
        # https://docs.djangoproject.com/en/5.0/ref/models/options/
        # sirve para indicar como se llamara la tabla en la base de datos
        db_table = 'platos'
