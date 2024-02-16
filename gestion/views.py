from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
