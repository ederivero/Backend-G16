from flask import Flask
from flask_migrate import Migrate
from variables import conexion
from dotenv import load_dotenv
# os > operating system
from os import environ
from models import *
from controllers import *
from flask_restful import Api
from flask_jwt_extended import JWTManager


# leear el archivo .env si existe y agregara todas las variables al entorno como si fuesen variables de entorno del sistema
# tiene que ir en la parte mas alta del archivo principal para que pueda ser utilizado en todo el proyecto
load_dotenv()

app = Flask(__name__)
api = Api(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
conexion.init_app(app)


JWTManager(app=app)
# Esto crea la utilizacion de las migraciones en nuestro proyecto de flask
Migrate(app=app, db=conexion)

# Agrego mis rutas
api.add_resource(InvitadosController, '/invitados')
api.add_resource(BarmanController, '/barman')
api.add_resource(LoginController, '/login')

if __name__ == "__main__":
    app.run(debug=True)
