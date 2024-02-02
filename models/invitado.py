from sqlalchemy import Column, types
from variables import conexion


class Invitado(conexion.Model):
    __tablename__ = 'invitados'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    dni = Column(type_=types.String(15), unique=True, nullable=False)
    nombre = Column(type_=types.String(30))
    apellido = Column(type_=types.String(100))
    telefono = Column(type_=types.String(15), nullable=True)
