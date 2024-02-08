from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError


# un decorador es la implementacion de una funcion dentro de otra funcion sin la necesidad de llamarlo o ejecutarlo dentro de la funcion
def validar_invitado(funcion):
    # wraps > envuelve la funcon o metodo donde vamos a utilizar esta funcion para devolvernos toda su configuracion
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        # valida que tengamos una jwt en nuestro request y si hay nos lo devuelve los valores decodificados
        data = verify_jwt_in_request()

        # xxxxxx.yyyyyy.zzzzz
        tipo = data[1].get('tipo')

        if not tipo:
            raise NoAuthorizationError('Token invalida')

        if tipo != 'Invitado':
            raise NoAuthorizationError('Usuario con permisos insuficientes')

        # si es de tipo Invitado
        # continuara con la funcion que va debajo del decorador
        return funcion(*args, **kwargs)

    # para indicar al decorador que la funcion que utilizara es el wrapper
    return wrapper


def validar_barman(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        data = verify_jwt_in_request()

        tipo = data[1].get('tipo')

        if not tipo:
            raise NoAuthorizationError('Token invalida')

        if tipo != 'Barman':
            raise NoAuthorizationError('Usuario con permisos insuficientes')

        return funcion(*args, **kwargs)

    return wrapper
