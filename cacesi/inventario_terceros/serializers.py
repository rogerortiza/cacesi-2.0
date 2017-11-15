from rest_framework import serializers
from .models import Extintores

class ExtintoresTercerosSerializer(serializers.ModelSerializer):
	area = serializers.StringRelatedField()
	foto = serializers.SerializerMethodField('get_foto_url')

	def get_foto_url(self, obj):
		if obj.foto is None:
			return "no-foto.png"
		else:
			return '%s' % (obj.foto.url)

	class Meta:
		model = Extintores
		fields = ("__all__")
