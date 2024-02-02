from flask_restful import Resource


class InvitadosController(Resource):
    # el metodo tiene que ser en minusculas sino no lo reconocera
    def post(self):
        print('Ingreso al post')

        return {
            'message': 'Invitado creado exitosamente'
        }
