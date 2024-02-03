from sqlalchemy import Column, types
from variables import conexion


class Trago(conexion.Model):
    # para indicar como se llamara esta tabla en la bd
    __tablename__ = 'tragos'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)

    nombre = Column(type_=types.Text, nullable=False)
    # server_default > sirve para indicar el valor por defecto A NIVEL DE BD en el caso que no se ingrese al momento de hacer una creacion
    # server_default solo acepta string o TextClause
    disponible = Column(type_=types.Boolean, server_default='1')
