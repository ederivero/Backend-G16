from flask_restful import Resource, request
from dtos import RegistrarInvitadoDTO
from requests import get
from os import environ
from variables import conexion
from models import Invitado


class InvitadosController(Resource):
    # el metodo tiene que ser en minusculas sino no lo reconocera
    def post(self):
        dto = RegistrarInvitadoDTO()
        try:
            data_serializada = dto.load(request.get_json())

            token_api_dni = environ.get('API_DNI')

            if not token_api_dni:
                # No hemos configurado la token para consumir el servicio de API DNI
                raise Exception('Falta configurar la token de API DNI')

            resultado = get(f"https://api.apis.net.pe/v2/reniec/dni?numero={data_serializada.get('dni')}",
                            headers={'Authorization': f'Bearer {token_api_dni}'})
            # convierte la informacion a un diccionario legible en python
            data_api = resultado.json()

            nuevo_invitado = Invitado(dni=data_serializada.get('dni'),
                                      nombre=data_api.get('nombres'),
                                      apellido=data_api.get('apellidoPaterno')
                                      + ' ' +
                                      data_api.get('apellidoMaterno'),
                                      telefono=data_serializada.get('telefono'))

            conexion.session.add(nuevo_invitado)
            conexion.session.commit()
            return {
                'message': 'Invitado creado exitosamente'
            }
        except Exception as e:
            print(e)
            return {
                'message': 'Error al crear el invitado',
                'content': e.args
            }
