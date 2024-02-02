from flask import Flask
from flask_migrate import Migrate
from variables import conexion
from dotenv import load_dotenv
# os > operating system
from os import environ
# leear el archivo .env si existe y agregara todas las variables al entorno como si fuesen variables de entorno del sistema
# tiene que ir en la parte mas alta del archivo principal para que pueda ser utilizado en todo el proyecto
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

conexion.init_app(app)

# Esto crea la utilizacion de las migraciones en nuestro proyecto de flask
Migrate(app=app, db=conexion)

if __name__ == "__main__":
    app.run(debug=True)
