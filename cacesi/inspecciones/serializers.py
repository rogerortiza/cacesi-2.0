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
	foto = serializers.SerializerMethodField('get_foto_url')

	def get_foto_url(self, obj):
		return '%s' % (obj.foto)


	class Meta:
		model = Extintores
		fields = ('__all__')
