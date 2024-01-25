from variables import conexion
from sqlalchemy import Column, types, ForeignKey


class DireccionModel(conexion.Model):
    id = Column(
        primary_key=True,
        autoincrement=True,
        type_=types.Integer)
    calle = Column(
        type_=types.Text
    )
    numero = Column(
        type_=types.String(20)
    )
    referencia = Column(
        type_=types.Text
    )
    predeterminada = Column(
        type_=types.Boolean,
        default=False  # default > si queremos colocar un valor por defecto al momento de crear
    )
    # Relaciones
    usuarioId = Column(ForeignKey(column='usuarios.id'),
                       nullable=False, name='usuario_id')
    __tablename__ = 'direcciones'
