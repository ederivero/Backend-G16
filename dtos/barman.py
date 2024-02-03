from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Barman
from marshmallow import Schema, fields


class RegistrarBarmanDTO(SQLAlchemyAutoSchema):
    class Meta:
        # pasara metadatos o informacion a la clase de la cual estamos heredando
        # model sirve para indicar con que modelo se basara para hacer las validaciones correspondientes
        model = Barman


class LoginBarmanDTO(Schema):
    # Crear un DTO en el cual solamente reciba el username y el password de manera obligatoria
    username = fields.String(required=True, error_messages={
        'required': 'El username es obligatorio'
    })
    password = fields.String(required=True, error_messages={
        'required': 'El password es obligatorio'
    })
