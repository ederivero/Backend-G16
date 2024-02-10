from sqlalchemy import Column, types, ForeignKey, orm
from variables import conexion
from enum import Enum
# func son funciones internas de sql
from sqlalchemy.sql import func


class EstadoPedidosEnum(Enum):
    ATENTIDO = 'ATENTIDO'
    EN_ESPERA = 'EN_ESPERA'
    PREPARANDO = 'PREPARANDO'
    PREPARADO = 'PREPARADO'


class Pedido(conexion.Model):
    __tablename__ = 'pedidos'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)

    fecha_creacion = Column(type_=types.DateTime,
                            server_default=func.now(), nullable=False)

    estado = Column(type_=types.Enum(EstadoPedidosEnum),
                    server_default=EstadoPedidosEnum.EN_ESPERA.value)

    invitadoId = Column(ForeignKey(column='invitados.id'),
                        nullable=False, name='invitado_id')

    barmanId = Column(ForeignKey(column='barmans.id'),
                      name='barman_id')

    # ahora en nuestra Invitado se creara un atributo virtual llamado pedidos y a su vez en el Pedido podremos ingresar a toda la instancia del Invitado por su atributo invitado (haciendo un inner join)
    invitado = orm.relationship(argument='Invitado', backref='pedidos')
