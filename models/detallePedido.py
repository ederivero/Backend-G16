from sqlalchemy import Column, types, ForeignKey
from variables import conexion


class DetallePedido(conexion.Model):
    __tablename__ = 'detalle_pedidos'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    cantidad = Column(type_=types.Integer, nullable=False)

    trago = Column(ForeignKey(column='tragos.id'),
                   name='trago_id', nullable=False)
    pedido = Column(ForeignKey(column='pedidos.id'),
                    name='pedido_id', nullable=False)
