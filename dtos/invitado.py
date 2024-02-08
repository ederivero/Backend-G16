from marshmallow import Schema, fields, validate


class RegistrarInvitadoDTO(Schema):
    # validamos que el dni sea entre 8 y 11 caracteres y sea puro numero
    dni = fields.String(
        required=True,
        validate=validate.Regexp(regex='^(?:\d{8}|\d{11})$',
                                 error='El dni tiene que tener 8 caracteres y todos deben de ser numeros'),
        error_messages={
            'required': 'El dni es obligatorio',
            'null': '',  # este mensaje se mostrara cuando el campo no puede ser nulo
            'validator_failed': ''  # cuando el validador falla y este no acepta su parametro de error
        })
    telefono = fields.String(
        required=True, validate=validate.Regexp(
            regex='^\d{9}$',
            error='El telefono tiene que tener 9 numeros'),
        error_messages={
            'required': 'El telefono es obligatorio'
        })


class LoginInvitadoDTO(Schema):
    dni = fields.String(
        required=True,
        validate=validate.Regexp(regex='^(?:\d{8}|\d{11})$',
                                 error='El dni tiene que tener 8 caracteres y todos deben de ser numeros'),
        error_messages={
            'required': 'El dni es obligatorio',
            'null': '',  # este mensaje se mostrara cuando el campo no puede ser nulo
            'validator_failed': ''  # cuando el validador falla y este no acepta su parametro de error
        })
