from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Pedido, DetallePedido, Trago
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


class TragoDTO(SQLAlchemyAutoSchema):
    class Meta:
        model = Trago
        # fields  sirve para indicar que atributos queremos utilizar, los que esten declarados seran los que se mostraran
        fields = ['nombre']


class DetallePedidoDTO(SQLAlchemyAutoSchema):
    trago = fields.Nested(nested=TragoDTO, attribute='trago')

    class Meta:
        model = DetallePedido
        fields = ['trago', 'cantidad']
        # si queremos mostrar las llaves foraneas de nuestro modelo entonces definimos el atributo include_fk con True
        # include_fk = True


class ListarPedidosDTO(SQLAlchemyAutoSchema):
    # cuando en un modelo tenemos una columna que va a ser de tipo enum tenemos que indicar a Marshmallow
    # tenemos que indicar que enum tiene que utilizar para hacer las conversiones correspondientes
    estado = EnumField(EstadoPedidosEnum)
    # Si colocamos un nombre diferente del atributo virtual entonces no hara match y por ende no mostrara la informacion, caso contrario si concuerda mostrara la informacion ,
    # en este caso como un pedido puede tener muchos detallePedidos tenemos que colocar el parametro many=True para que lo itere
    # si quisieramos cambiar el nombre a mostrar entonces deberiamos colocar el parametro attribute PERO si hacemos esto, entonces el atributo include_relationships ya no debe estar presente en el DTO
    # se recomienda colocar el parametro attribute cuando el nombre del atributo es diferente
    detallePedidoasas = fields.Nested(
        nested=DetallePedidoDTO, many=True, attribute='detallePedidos')

    class Meta:
        model = Pedido
        # Buscara si este modelo tiene relationships y si los tiene los agregara al DTO
        # include_relationships = True
