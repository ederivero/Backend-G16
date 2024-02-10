from models import Trago
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class TragoDTO(SQLAlchemyAutoSchema):
    class Meta:
        model = Trago
