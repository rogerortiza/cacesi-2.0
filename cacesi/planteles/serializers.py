from rest_framework import serializers
"""
from .models import Areas

class AreasSerializer(serializers.ModelSerializer):
	cliente = serializers.StringRelatedField()
	plano = serializers.SerializerMethodField('get_plano_url')

	def get_plano_url(self, obj):
		return '%s' % (obj.plano.url)
	class Meta:
		model = Areas
		fields = ('__all__')
"""
