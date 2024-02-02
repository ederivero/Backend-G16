# El archivo __init__ sirve para al momento de importar la carpeta este archivo mostrara la configuracion inicial de la carpeta

# Para importar un archivo dentro de la carpeta se puede hacer de la siguiente manera
from .barman import Barman
# o de esta otra manera
from models.invitado import Invitado
from .trago import Trago
from models.pedido import Pedido
from .detallePedido import DetallePedido
