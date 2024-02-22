from rest_framework import serializers
from .models import Plato


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        # el modelo en el cual se utilizara de referencia para convertir la data de la bd y viceversa
        model = Plato
        # fields > indicar que columnas quiero mostrar
        # exclude > indicar que columnas quiero excluir
        # NOTA: solo se puede utilizar uno de los dos, no los dos al mismo tiempo porque da errores
        # fields = ['id', 'nombre', 'foto']
        # si estoy utilizando todos los atributos del modelo
        fields = '__all__'

        # exclude = ['id']
