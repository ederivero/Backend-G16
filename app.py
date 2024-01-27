from flask import Flask, request
from variables import conexion
from models.usuario import UsuarioModel
from models.direccion import DireccionModel
from flask_migrate import Migrate
from datetime import datetime
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

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


class UsuarioDTO(Schema):
    nombre = fields.Str(required=True)
    apellido = fields.Str()
    # hace la validacion que cumpla el patron xxxxxxxxx@yyyyyy.zzz
    correo = fields.Email(required=True)
    fechaNacimiento = fields.Date()
    sexo = fields.Str()


class UsuarioModelDto(SQLAlchemyAutoSchema):
    class Meta:
        # model sirve para indicar desde que modelo nos vamos a referenciar para jalar toda la configuracion de nuestro DTO
        # en base a las columnas seteara las configuraciones para pedir el tipo de dato necesario, si es que null o no, si es AI ya no lo pide ni las llaves primarias y toda la configuracion de la tabla
        model = UsuarioModel


@app.route('/usuarios', methods=['GET'])
def gestionarUsuarios():
    # session > un actividad que tenemos con la base de datos
    # SELECT * FROM usuarios;
    resultado = conexion.session.query(UsuarioModel).all()
    validador = UsuarioModelDto()
    # el metodo dump solamente convertira un usuario a la vez
    # a no ser que le coloquemos el parametro que le estamos pasando muchos
    # many indicamos que le estamos pasando una lista de registros por lo que los tendra que iterar y convertir cada uno de ellos
    usuarios = validador.dump(resultado, many=True)
    # usuarios = []

    # for usuario in resultado:
    #     usuarios.append({
    #         'id': usuario.id,
    #         'nombre': usuario.nombre,
    #         'apellido': usuario.apellido,
    #         'correo': usuario.correo,
    #         'sexo': usuario.sexo,
    #         # string from time > convertir un valor de tipo fecha y hora a string pero colocando el formato
    #         # %Y > Devolvera el año
    #         # %y > devolver los dos ultimos digitos del año
    #         # %m > devuelve los digitos del mes
    #         # %B > devuelve el nombre del mes
    #         # %b > devuelve las tres primeras letras del mes
    #         # %d > dia del mes
    #         # %H > hora
    #         # %M > minutos
    #         # %S > segundos
    #         'fechaNacimiento': datetime.strftime(usuario.fechaNacimiento, '%Y-%m-%d')
    #     })

    return {
        'content': usuarios
    }, 200


@app.route('/usuario', methods=['POST'])
def crearUsuario():
    try:
        # capturar la informacion
        data = request.get_json()
        # validador = UsuarioDTO()
        validador = UsuarioModelDto()
        # load > pasarle la informacion y ver si es correcta o no y si si lo es devolvera la informacion transformada
        # si la informacion es incorrecta entonces lanzara un error y este lo podremos recibir en el except
        dataValidada = validador.load(data)

        # creo mi nuevo usuario
        nuevoUsuario = UsuarioModel(**dataValidada)

        # Agregar este nuevo registro a la base de datos de manera temporal
        conexion.session.add(nuevoUsuario)

        print('Antes del commit', nuevoUsuario.id)
        # commit sirve para transacciones y permite que todos los cambios realizados en la base de datos permanezcan de manera persistente
        conexion.session.commit()
        print('Despues del commit', nuevoUsuario.id)

        # dump > sirve para convertir una instancia de la clase a un diccionario para poder devolverlo
        usuarioCreado = validador.dump(nuevoUsuario)
        # usuarioCreado = {
        #     'id': nuevoUsuario.id,
        #     'nombre': nuevoUsuario.nombre,
        #     'apellido': nuevoUsuario.apellido,
        #     'correo': nuevoUsuario.correo,
        #     'sexo': nuevoUsuario.sexo,
        #     'fechaNacimiento': datetime.strftime(nuevoUsuario.fechaNacimiento, '%Y-%m-%d')
        # }
        return {
            'message': 'Usuario creado exitosamente',
            'content': usuarioCreado  # mostrar el usuario recien creado
        }, 201

    except Exception as error:
        return {
            'message': 'Error al crear el usuario',
            'content': error.args
        }, 400


@app.route('/usuario/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def gestionarUsuario(id):
    if request.method == 'GET':
        # SELECT * FROM usuarios WHERE id = .... LIMIT 1;
        usuarioEncontrado = conexion.session.query(
            UsuarioModel).filter_by(id=id).first()
        # si queremos definir que columnas utilizar al momento de hacer la consultar
        # SELECT correo, nombre FROM usuarios;
        prueba = conexion.session.query(
            UsuarioModel).with_entities(UsuarioModel.correo, UsuarioModel.nombre).all()
        print(prueba)

        if usuarioEncontrado is None:
            return {
                'message': 'El usuario no existe'
            }, 404

        # usar el UsuarioModelDto para devolver la informacion
        serializador = UsuarioModelDto()
        resultado = serializador.dump(usuarioEncontrado)
        return {
            'content': resultado
        }, 200

    elif request.method == 'PUT':
        # SELECT id FROM usuarios WHERE id = .... LIMIT 1;
        usuarioEncontrado = conexion.session.query(UsuarioModel).with_entities(
            UsuarioModel.id).filter_by(id=id).first()

        # if usuarioEncontrado:  > si el usuario no esta vacio (si hay un usuario)
        # Si el usuario no existe:
        # if usuarioEncontrado == None:
        if not usuarioEncontrado:
            return {
                'message': 'Usuario no existe'
            }, 404

        # Si existe el usuario
        validador = UsuarioModelDto()
        # validamos si la informacion enviada es la correcta
        dataValidada = validador.load(request.get_json())
        # UPDATE usuarios SET nombre = '...' , apellido = '....' WHERE id = ...;
        resultado = conexion.session.query(UsuarioModel).filter_by(
            id=id).update(dataValidada)

        # Para guardar los datos de manera permanente
        conexion.session.commit()
        return {
            'message': 'Usuario actualizado exitosamente'
        }, 200

    elif request.method == 'DELETE':
        usuarioEncontrado = conexion.session.query(UsuarioModel).with_entities(
            UsuarioModel.id).filter_by(id=id).first()

        if not usuarioEncontrado:
            return {
                'message': 'Usuario no existe'
            }, 404

        conexion.session.query(UsuarioModel).filter_by(id=id).delete()

        conexion.session.commit()

        # cuando hacemos una eliminacion no se devuelve nada y se utiliza el estado 204 (NO CONTENT)
        return {}, 204


@app.route('/usuario/deshabilitar/<int:id>', methods=['DELETE'])
def deshabilitarUsuario(id):
    usuarioEncontrado = conexion.session.query(UsuarioModel).with_entities(
        UsuarioModel.id).filter_by(id=id).first()

    if not usuarioEncontrado:
        return {
            'message': 'Usuario no existe'
        }, 404

    conexion.session.query(UsuarioModel).filter_by(
        id=id).update({'activo': False})

    conexion.session.commit()

    return {
        'message': 'Usuario inhabilitado exitosamente'
    }


@app.route('/')
def inicial():
    return {
        'message': 'Bienvenido a mi API de usuarios'
    }


if __name__ == '__main__':
    app.run(debug=True)
