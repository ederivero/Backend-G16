from flask import Flask
from flask_migrate import Migrate
from variables import conexion, clienteTwilio
# os > operating system
from os import environ
from models import *
from controllers import *
from flask_restful import Api
from flask_jwt_extended import JWTManager, get_jwt_identity
from datetime import timedelta
from decoradores import validar_barman
from models.pedido import EstadoPedidosEnum
from flasgger import Swagger
# load convierte la informacion de un json a un diccionario
from json import load

app = Flask(__name__)
api = Api(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# configuraciones para mi JWT
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1, minutes=30)  # 90

conexion.init_app(app)

swaggerConfig = {
    'headers': [],  # las cabeceras que podra aceptar nuestra documentacion
    'specs': [
        {
            'endpoint': '',  # el endpoint inicial de nuestra documentacion
            # mi ruta base de mi documentacion (hacia donde hara los requests)
            'route': '/'
        }
    ],
    # Donde cargara los archivos staticos de swagger para la intefaz grafica
    # para indicar esto tenemos que colocar la opcion 'swagger_ui': True sino podemos obviar este paso
    'static_url_path': '/flassger_static',
    # el endpoint en el cual ahora estara alojada la documentacion de swagger
    'specs_route': '/documentacion'

}

swaggerTemplate = load(open('swagger_template.json'))
Swagger(app=app, template=swaggerTemplate, config=swaggerConfig)

JWTManager(app=app)
# Esto crea la utilizacion de las migraciones en nuestro proyecto de flask
Migrate(app=app, db=conexion)

# Agrego mis rutas
api.add_resource(InvitadosController, '/invitados')
api.add_resource(BarmanController, '/barman')
api.add_resource(LoginController, '/login')
api.add_resource(LoginInvitadoController, '/login-invitado')
api.add_resource(PedidosController, '/pedidos')
api.add_resource(TragosController, '/tragos')


@app.route('/preparar-pedido/<int:id>', methods=['POST'])
@validar_barman
def prepararPedido(id):
    """
    file: prepararPedido.yml
    """
    barmanId = get_jwt_identity()

    # Primero buscar si existe el pedido con ese id
    # Buscar si el pedido aun no tiene un barman seleccionado
    # SELECT * FROM pedidos WHERE id = ... AND barman IS NULL;
    pedido_encontrado = conexion.session.query(Pedido).filter(
        Pedido.id == id, Pedido.barmanId == None).first()
    # si lo tiene entonces retornar un 400 e indicar que el pedido ya tiene un barman
    if not pedido_encontrado:
        return {
            'message': 'El pedido a buscar no existe o ya fue tomado por otro barman'
        }, 400
    # Actualizar el pedido y configurar el barman y cambiar el estado del pedido a 'PREPARANDO'

    # UPDATE pedidos SET barman_id = .... AND estado = 'PREPARANDO' WHERE id = ...;
    conexion.session.query(Pedido).filter_by(
        id=pedido_encontrado.id).update({
            Pedido.barmanId: barmanId,
            Pedido.estado: EstadoPedidosEnum.PREPARANDO
        })

    conexion.session.commit()
    return {
        'message': 'Pedido configurado exitosamente'
    }, 200


@app.route('/pedido-preparado/<int:id>', methods=['POST'])
@validar_barman
def pedidoPreparado(id):
    barmanId = get_jwt_identity()
    # buscar el pedido con el id y con el barmanId
    pedido_encontrado = conexion.session.query(Pedido).filter(
        Pedido.id == id,  # existe el pedido
        Pedido.barmanId == barmanId,  # le pertenece al barman
        # el pedido tiene que estar preparandose
        Pedido.estado == EstadoPedidosEnum.PREPARANDO
    ).first()
    # Si no existe el pedido indicar que no existe

    if not pedido_encontrado:
        return {
            'message': 'Pedido no existe o no tienes los permisos necesarios'
        }, 400
    conexion.session.query(Pedido).filter(Pedido.id == id).update(
        {Pedido.estado: EstadoPedidosEnum.PREPARADO})
    conexion.session.commit()

    mensaje = clienteTwilio.messages.create(
        from_='+16593365113',
        to=f'+51{pedido_encontrado.invitado.telefono}',
        body=f'''Hola {pedido_encontrado.invitado.nombre}.
Tu pedido de la barra ya esta listo, puedes retirarlo 🍸''',
    )
    # sid> identificador del mensaje por si lo queremos validar en la pagina de twilio
    print(mensaje.sid)
    return {
        'message': 'Pedido completado'
    }, 200


if __name__ == "__main__":
    app.run(debug=True)
