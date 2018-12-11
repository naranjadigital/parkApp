from rest_framework import serializers

from backoffice.models import *


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('__all__')


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('__all__')


class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = ('__all__')


class EstacionamientoSerializer(serializers.ModelSerializer):
    departamento_nombre = serializers.CharField(source='departamento')
    provincia_nombre = serializers.CharField(source='provincia')
    distrito_nombre = serializers.CharField(source='distrito')

    class Meta:
        model = Estacionamiento
        fields = ['nombre', 'departamento_nombre', 'provincia_nombre', 'distrito_nombre']