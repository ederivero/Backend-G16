from flask import Flask, request
from uuid import uuid4
from flask_cors import CORS


app = Flask(__name__)
# Si lo dejamos sin ninguna configuracion adicional lo que va a suceder es que en teoria va a permitir que todos los origenes y todos los metodos y todos los headers sean permitidos
CORS(app=app,
     # que metodos pueden acceder a mi API
     methods=['GET', 'POST', 'PUT', 'DELETE'],
     # desde que dominios se puede acceder a mi API, si queremos que cualquier origen se conecte colocamos el '*'
     origins=['http://localhost:5500', 'http://127.0.0.1:5500'],
     # que headers (cabeceras) pueden enviar a mi API, '*'
     allow_headers=['accept', 'authorization', 'content-type']
     )

productos = [
    {
        'id': uuid4(),
        'nombre': 'Palta fuerte',
        'precio': 7.50,
        'disponibilidad': True
    },
    {
        'id': uuid4(),
        'nombre': 'Lechuga Carola',
        'precio': 1.50,
        'disponibilidad': True
    }
]


@app.route('/', methods=['GET'])
def inicio():
    return {
        'message': 'Bienvenido a la API de Productos'
    }, 200


@app.route('/productos', methods=['GET'])
def gestionProductos():
    return {
        'message': 'Los productos son',
        'content': productos
    }, 200


# si voy a recibir un parametro dinamico (que va a cambiar su valor) y eso lo voy a manejar internamente
# Los formatos que puedo parsear son:
# string > para recibir textos
# int > para recibir solo numeros
# float > para recibir numeros con punto decimal
# path > que son string pero tbn aceptan slashes /
# uuid > aceptar UUID's
# al colocar un parseador si el formato que me envia el cliente no cumple con este conversion no aceptara la peticion
# si yo defino un parametro dinamico ese parametro lo tengo que recibir en la funcion
@app.route('/producto/<uuid:id>', methods=['GET'])
def gestionProducto(id):
    print(id)
    # tenemos una lista de productos en el cual en cada posicion tenemos un diccionario y una llave llamada id
    # iteren esos productos y vean si existe el producto con determinado id
    # si no existe entonces retornar un message que diga 'Producto no existe' con un estado 404
    # PISTA: hacer un for con if y else dentro de el
    for producto in productos:
        if producto['id'] == id:
            return {
                'content': producto
            }, 200

    return {
        'message': 'El producto no existe'
    }, 404


@app.route('/producto', methods=['POST'])
def crearProducto():
    # convierte la data del body a un dictionary si el body es un JSON
    data = request.get_json()
    # antes de guardar la informacion en los productos agregarle el id
    data['id'] = uuid4()

    productos.append(data)
    return {
        'content': data
    }, 201  # Created


if __name__ == '__main__':
    app.run(debug=True)
