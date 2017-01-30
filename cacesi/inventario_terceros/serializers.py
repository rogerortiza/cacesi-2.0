from rest_framework import serializers
from .models import Extintores

class ExtintoresTercerosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Extintores
		fields = ("__all__")