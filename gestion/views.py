from django.shortcuts import render


def vistaPrueba(request):
    return render(request=request, template_name='prueba.html')
