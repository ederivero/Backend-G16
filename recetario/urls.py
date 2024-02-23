"""
URL configuration for recetario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# importa todas las variables declaradas en mi archivo settings.py
from django.conf import settings
# genera mi vista para poder acceder a la documentacion
from drf_yasg.views import get_schema_view
from drf_yasg import openapi  # es la herramienta que utiliza swagger por detras

swagger_view = get_schema_view(
    openapi.Info(
        title='API de Recetario',
        default_version='v1',
        description='API para gestionar el uso de un recetario con autenticacion',
        contact=openapi.Contact(name='Eduardo de Rivero',
                                email='ederiveroman@gmail.com')
    ),
    public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    # si queremos agregar un archivo con otras rutas entonces usaremos el metodo include
    path('gestion/', include('gestion.urls')),
    path('documentacion/', swagger_view.with_ui('swagger', cache_timeout=0))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# agregando a unas rutas del proyecto la ruta 'static/' con todo el contenido declarado en media_root en la carpeta 'archivos'
