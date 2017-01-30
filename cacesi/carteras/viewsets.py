from rest_framework import viewsets	
from .serializers import ClientesSerializer
from .models import Clientes

class ClientesViewSet(viewsets.ModelViewSet):
	queryset = Clientes.objects.all()
	serializer_class = ClientesSerializer