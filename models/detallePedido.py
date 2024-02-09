from sqlalchemy import Column, types, ForeignKey, orm
from variables import conexion


class DetallePedido(conexion.Model):
    __tablename__ = 'detalle_pedidos'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    cantidad = Column(type_=types.Integer, nullable=False)

    tragoId = Column(ForeignKey(column='tragos.id'),
                     name='trago_id', nullable=False)
    pedidoId = Column(ForeignKey(column='pedidos.id'),
                      name='pedido_id', nullable=False)

    # el nombre del modelo en el cual quiero crear mi relacion virtual
    # NOTA: esto no afecta en nada el funcionamiento a nivel de base de datos
    # backref > creara un atributo virtual en nuestro modelo en el cual estamos creando la relacion, es decir ahora en DetallePedido tendremos un nuevo atributo llamado 'detallePedidos' que este nos devolvera todos sus detalles pedidos
    pedido = orm.relationship('Pedido', backref='detallePedidos')

    trago = orm.relationship('Trago', backref='tragoPedidos')
