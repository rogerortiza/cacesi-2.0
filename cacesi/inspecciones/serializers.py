from rest_framework import serializers
from plantilla.models import Empleados
from inventario_terceros.models import Extintores as ExtintoresTerceros
from inspecciones.models import Extintores

class ExtintorSerializer(serializers.ModelSerializer):
	area = serializers.StringRelatedField()

	class Meta:
		model = ExtintoresTerceros
		fields = ('__all__')

class ExtintoresSerializer(serializers.ModelSerializer):
	empleado = serializers.StringRelatedField()
	extintor = ExtintorSerializer()

	class Meta:
		model = Extintores
		fields = ('__all__')
