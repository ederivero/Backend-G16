from marshmallow import Schema, fields


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
class ItemPedidoDTO(Schema):
    tragoId = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)


class CrearPedidoDTO(Schema):
    detalle = fields.List(fields.Nested(ItemPedidoDTO))
