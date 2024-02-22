from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Plato
from .serializers import PlatoSerializer


def vistaPrueba(request):
    usuario = {
        'nombre': 'Eduardo',
        'apellido': 'de Rivero',
        'hobbies': [
            {
                'descripcion': 'Ir al cine'
            },
            {
                'descripcion': 'Viajar'
            }
        ]
    }
    return render(request=request, template_name='prueba.html', context=usuario)


def mostrarRecetas(request):
    return render(request, 'mostrarRecetas.html')


# siempre en una funcion que trabaja como controlador recibiremos el request (informacion entrante del cliente)
@api_view(http_method_names=['GET', 'POST'])
def controlladorInicial(request):
    return Response(data={
        'message': 'Bienvenido a mi API'
    })


class PlatosController(APIView):
    def get(self, request):
        # SELECT * FROM platos
        resultado = Plato.objects.all()
        print(resultado)
        # instance > cuando tenemos instancias del modelo para serializar
        # data > cuando tenemos informacion que vamos a guardar, modificar en la base de datos proveniente del cliente
        serializador = PlatoSerializer(instance=resultado, many=True)
        return Response(data={
            'message': 'Me hicieron get',
            'content': serializador.data
        })
