from django.contrib.auth.models import User
from rest_framework import serializers
from personas.models import Persona, automovile,fabricante

class AutomovilSerializer(serializers.ModelSerializer):
    propietario_nombre = serializers.CharField(source='propietario.nombre', read_only=True)
    fabricante_nombre = serializers.CharField(source='fabricante.nombre', read_only=True)

    class Meta:
        model = automovile
        fields = ['id', 'url','propietario','propietario_nombre', 'marca_auto', 'color_auto', 'placa_auto', 'fecha_compra','fabricante','fabricante_nombre']


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'url', 'nombre', 'apellido', 'cedula']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    persona = PersonaSerializer(source='persona_set.first', read_only=True, allow_null=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'persona']

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = fabricante
        fields = ['id', 'nombre']