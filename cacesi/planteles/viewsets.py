from rest_framework import viewsets
from .serializers import AreasSerializer
from .models import Areas

class AreasViewSet(viewsets.ModelViewSet):
	queryset = Areas.objects.all()
	serializer_class = AreasSerializer

	def get_queryset(self):
		return self.queryset.filter(cliente_id = self.kwargs['cliente_pk'])