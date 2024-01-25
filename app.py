from flask import Flask
from variables import conexion
from models.usuario import UsuarioModel
from models.direccion import DireccionModel

app = Flask(__name__)
# print(app.config)
# app.config almacenara todas las variables que se utilizan en el proyecto de Flask
# NOTA: No confundir con las variables de entorno!
# ahora agregamos una nueva llave a nuestra variables de configuracion
# dialecto://usuario:contraseña@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/alumnos'
# Inicializar la conexion a nuestra BD
# al momento de pasarle la aplicacion de flask en esta se encontraras la cadena de conexion a la bd
conexion.init_app(app)


# before_request > se mandara a llamar a esta funcionabilidad antes de cualquier request (peticion)
@app.before_request
def inicializacion():
    # create_all > crea todas las tablas que no se han creado en la base de datos
    conexion.create_all()


@app.route('/')
def inicial():
    return {
        'message': 'Bienvenido a mi API de usuarios'
    }


if __name__ == '__main__':
    app.run(debug=True)
