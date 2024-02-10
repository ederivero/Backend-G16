from flask_restful import Resource
from models import Trago
from variables import conexion
from dtos import TragoDTO


class TragosController(Resource):
    def get(self):
        """
        Listado de los tragos
        ---
        operationId: list_tragos
        description: Lista todos los tragos disponibles
        tags:
            - Trago
        responses:
            200:
                description: Listado de tragos disponibles
                schema:
                    $ref: '#/definitions/Trago'
        """
        info = conexion.session.query(Trago).all()
        dto = TragoDTO()

        tragos = dto.dump(info, many=True)
        return {
            'content': tragos
        }
