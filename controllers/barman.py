from flask_restful import Resource, request
from variables import conexion
from models import Barman
from dtos import RegistrarBarmanDTO, LoginBarmanDTO
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token


class BarmanController(Resource):
    def post(self):
        dto = RegistrarBarmanDTO()
        try:
            data_validada = dto.load(request.get_json())
            # password necesita ser hasheada (generar un hash de un texto)
            salt = gensalt(rounds=10)

            # convertir la password a tipo de dato bytes
            password_bytes = bytes(data_validada.get('password'), 'utf-8')

            # decode > convierte el formato bytes a formato string
            password_hasheada = hashpw(password_bytes, salt).decode('utf-8')

            nuevo_barman = Barman(username=data_validada.get('username'),
                                  nombre=data_validada.get('nombre'),
                                  password=password_hasheada)

            conexion.session.add(nuevo_barman)
            conexion.session.commit()

            return {
                'message': 'Barman registrado exitosamente'
            }, 201
        except Exception as e:
            return {
                'message': 'Error al registrar al barman',
                'content': e.args
            }, 400


class LoginController(Resource):
    def post(self):
        dto = LoginBarmanDTO()
        try:
            data_validada = dto.load(request.get_json())
            barman_encontrado = conexion.session.query(Barman).filter_by(
                username=data_validada.get('username')).first()

            if not barman_encontrado:
                raise Exception('El barman no existe')

            # checkpw indicara si es o no es la password (True o False)
            validar_password = checkpw(bytes(data_validada.get('password'), 'utf-8'),
                                       bytes(barman_encontrado.password, 'utf-8'))

            if not validar_password:
                raise Exception('El password es incorrecto')

            # identity > sirve para indicar a que usuario le pertenece esa token
            token = create_access_token(identity=barman_encontrado.id)
            return {
                'message': 'Bienvenido',
                'content': token
            }
        except Exception as e:
            return {
                'message': 'Error al autenticar al barman',
                'content': e.args
            }, 400
