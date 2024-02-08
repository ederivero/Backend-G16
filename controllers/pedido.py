from flask_restful import Resource, request
from models import Pedido
from flask_jwt_extended import get_jwt_identity, jwt_required


class PedidosController(Resource):

    # cuando queremos que un controlador requiera de manera obligatoria una token
    @jwt_required()
    def post(self):
        # para acceder al identity configurado en la creacion de la token
        identificacion = get_jwt_identity()
        print(identificacion)
        return {
            'message': ''
        }
