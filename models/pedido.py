from sqlalchemy import Column, types, ForeignKey
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

    estado = Column(type_=types.Enum(EstadoPedidosEnum))

    invitado = Column(ForeignKey(column='invitados.id'),
                      nullable=False, name='invitado_id')

    barman = Column(ForeignKey(column='barmans.id'),
                    nullable=False, name='barman_id')
