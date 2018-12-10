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