import datetime
from django.contrib.auth.models import User
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
	usuario = models.OneToOneField(User, blank = True, null=True, on_delete = models.CASCADE )
	position = GeopositionField()

	def __str__(self):
		return self.nombre

class Proveedores(models.Model):
	class Meta:
		verbose_name_plural = "Proveedores"

	GIRO = {
		('1', 'Maquinaria'),
		('2', 'Equipos Contra Incendios'),
		('3', 'Equipos de Seguridad')
	}

	id = models.AutoField(primary_key = True)
	codigo = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	giro = models.CharField(max_length=100, choices = GIRO)
	direccion = models.CharField(blank=True, max_length=100)
	telefono = models.CharField(blank=True, max_length=12)
	pagina_web = models.CharField(blank=True, max_length=100)
	facebook = models.CharField(blank=True, max_length=100)
	twitter = models.CharField(blank=True, max_length=100)
	fecha_registro = models.DateField(default=datetime.datetime.today)

	def __str__(self):
		return self.nombre

class Contactos_Proveedores(models.Model):
	class Meta:
		verbose_name_plural = "Contactos del Proveedor"

	id = models.AutoField(primary_key = True)
	proveedor = models.ForeignKey(Proveedores)
	nombre = models.CharField(max_length=100)
	puesto = models.CharField(blank=True, max_length=100)
	telefono_oficina = models.CharField(blank=True, max_length=12)
	celular = models.CharField(blank=True, max_length=12)
	email = models.EmailField(blank = True)
	fecha_alta = models.DateField(default=datetime.datetime.today)
