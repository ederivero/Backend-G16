from rest_framework import serializers
from .models import Plato, Ingrediente, Preparacion


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


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class PreparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preparacion
        fields = '__all__'


class PlatoConIngredientesYPreparacionesSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)
    # si queremos definir un atributo que no existe en nuestro modelo pero queremos utilizar un atributo como referencia entonces tenemos que definir el parametro source
    pasos = PreparacionSerializer(many=True, source='preparaciones')

    class Meta:
        model = Plato
        fields = '__all__'
