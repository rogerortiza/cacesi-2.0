from rest_framework import viewsets	
from .serializers import ExtintoresTercerosSerializer
from .models import Extintores

class ExtintoresTercerosViewSet(viewsets.ModelViewSet):
	queryset = Extintores.objects.all()
	serializer_class = ExtintoresTercerosSerializer

	def get_queryset(self):
		if 'cliente_pk' in self.kwargs:
			param = self.kwargs['cliente_pk']
		else:
			param = 1

		return self.queryset.filter(cliente_id = param)