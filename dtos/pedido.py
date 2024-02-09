from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Pedido
from models.pedido import EstadoPedidosEnum
from marshmallow_enum import EnumField


class ItemPedidoDTO(Schema):
    tragoId = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)


class CrearPedidoDTO(Schema):
    # {
    #     "detalle": [
    #         {
    #             "tragoId": 1,
    #             "cantidad": 2
    #         },
    #         {
    #             "tragoId": 2,
    #             "cantidad": 3
    #         },
    #         {
    #             "tragoId": 3,
    #             "cantidad": 1
    #         }
    #     ]
    # }
    detalle = fields.List(fields.Nested(ItemPedidoDTO))


class ListarPedidosDTO(SQLAlchemyAutoSchema):
    # cuando en un modelo tenemos una columna que va a ser de tipo enum tenemos que indicar a Marshmallow
    # tenemos que indicar que enum tiene que utilizar para hacer las conversiones correspondientes
    estado = EnumField(EstadoPedidosEnum)

    class Meta:
        model = Pedido
        # Buscara si este modelo tiene relationships y si los tiene los agregara al DTO
        include_relationships = True
