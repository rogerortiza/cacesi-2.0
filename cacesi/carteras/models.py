from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.
class Clientes(models.Model):
	class Meta:
		verbose_name_plural='Clientes'
		
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 140)
	razon_social = models.CharField(max_length = 140)
	rfc = models.CharField(max_length=20)
	sucursal = models.CharField(max_length = 140)
	codigo = models.CharField(max_length = 20)
	giro = models.CharField(max_length = 140)
	calle = models.CharField(max_length = 140)
	municipio = models.CharField(max_length = 140)
	estado = models.CharField(max_length = 60)
	pais = models.CharField(max_length = 60, default="Mexico")
	region = models.IntegerField()
	telefono = models.CharField(max_length = 20)
	email = models.CharField(max_length = 60)
	pagina_web = models.CharField(max_length = 140)
	logo = models.ImageField(upload_to = "static/logosClientes")
	position = GeopositionField()