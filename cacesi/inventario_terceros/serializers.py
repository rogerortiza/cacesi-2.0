from rest_framework import serializers
from .models import Extintores

class ExtintoresTercerosSerializer(serializers.ModelSerializer):
	area = serializers.StringRelatedField()
	cliente = serializers.StringRelatedField()
	
	class Meta:
		model = Extintores
		fields = ("__all__")