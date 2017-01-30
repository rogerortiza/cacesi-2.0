from rest_framework import viewsets
from inspecciones.serializers import ExtintoresSerializer
from inspecciones.models import Extintores

class ExtintoresViewSet(viewsets.ModelViewSet):
	queryset = Extintores.objects.all()
	serializer_class = ExtintoresSerializer

	def get_queryset(self):
		return self.queryset.filter(extintor__cliente_id = self.kwargs['cliente_pk'])