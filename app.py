from flask import Flask, request
from variables import conexion
from models.usuario import UsuarioModel
from models.direccion import DireccionModel
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
# print(app.config)
# app.config almacenara todas las variables que se utilizan en el proyecto de Flask
# NOTA: No confundir con las variables de entorno!
# ahora agregamos una nueva llave a nuestra variables de configuracion
# dialecto://usuario:contraseña@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/alumnos'
# Inicializar la conexion a nuestra BD
# al momento de pasarle la aplicacion de flask en esta se encontraras la cadena de conexion a la bd
conexion.init_app(app)

# Migrate sirve para comenzar a registrar los cambios en nuestra base de datos realizados desde nuestro ORM
Migrate(app=app, db=conexion)

# # before_request > se mandara a llamar a esta funcionabilidad antes de cualquier request (peticion)
# @app.before_request
# def inicializacion():
#     # drop_all > elimina todas las tablas y sus datos y perdemos la informacion
#     conexion.drop_all()
#     # create_all > crea todas las tablas que no se han creado en la base de datos
#     conexion.create_all()


@app.route('/usuarios', methods=['GET'])
def gestionarUsuarios():
    # session > un actividad que tenemos con la base de datos
    # SELECT * FROM usuarios;
    resultado = conexion.session.query(UsuarioModel).all()
    usuarios = []

    for usuario in resultado:
        usuarios.append({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'correo': usuario.correo,
            'sexo': usuario.sexo,
            # string from time > convertir un valor de tipo fecha y hora a string pero colocando el formato
            # %Y > Devolvera el año
            # %y > devolver los dos ultimos digitos del año
            # %m > devuelve los digitos del mes
            # %B > devuelve el nombre del mes
            # %b > devuelve las tres primeras letras del mes
            # %d > dia del mes
            # %H > hora
            # %M > minutos
            # %S > segundos
            'fechaNacimiento': datetime.strftime(usuario.fechaNacimiento, '%Y-%m-%d')
        })

    return {
        'content': usuarios
    }, 200


@app.route('/usuario', methods=['POST'])
def crearUsuario():
    try:
        # capturar la informacion
        data = request.get_json()
        # creo mi nuevo usuario
        nuevoUsuario = UsuarioModel(**data)

        # Agregar este nuevo registro a la base de datos de manera temporal
        conexion.session.add(nuevoUsuario)

        print('Antes del commit', nuevoUsuario.id)
        # commit sirve para transacciones y permite que todos los cambios realizados en la base de datos permanezcan de manera persistente
        conexion.session.commit()
        print('Despues del commit', nuevoUsuario.id)

        usuarioCreado = {
            'id': nuevoUsuario.id,
            'nombre': nuevoUsuario.nombre,
            'apellido': nuevoUsuario.apellido,
            'correo': nuevoUsuario.correo,
            'sexo': nuevoUsuario.sexo,
            'fechaNacimiento': datetime.strftime(nuevoUsuario.fechaNacimiento, '%Y-%m-%d')
        }
        return {
            'message': 'Usuario creado exitosamente',
            'content': usuarioCreado  # mostrar el usuario recien creado
        }, 201

    except Exception as error:
        return {
            'message': 'Error al crear el usuario',
            'content': error.args
        }


@app.route('/')
def inicial():
    return {
        'message': 'Bienvenido a mi API de usuarios'
    }


if __name__ == '__main__':
    app.run(debug=True)
