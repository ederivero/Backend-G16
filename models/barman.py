from sqlalchemy import Column, types
from variables import conexion


class Barman(conexion.Model):
    __tablename__ = 'barmans'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    username = Column(type_=types.String(100), unique=True, nullable=False)
    password = Column(type_=types.Text, nullable=True)
    nombre = Column(type_=types.Text, nullable=True)
