import datetime
from django.contrib.auth.models import User
from django.db import models
from geoposition.fields import GeopositionField


# Create your models here.
class Clientes(models.Model):
	class Meta:
		verbose_name="Cliente"
		verbose_name_plural='Clientes'

	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 140)
	razon_social = models.CharField(max_length = 140)
	rfc = models.CharField(max_length=20)
	sucursal = models.CharField(max_length = 140)
	codigo = models.CharField(max_length = 20)
	giro = models.CharField(max_length = 140)
	calle = models.CharField(max_length = 140)
	colonia = models.CharField(max_length=100)
	municipio = models.CharField(max_length = 140)
	estado = models.CharField(max_length = 60)
	cp = models.CharField(blank=True, max_length=5)
	pais = models.CharField(max_length = 60, default="Mexico")
	region = models.IntegerField()
	telefono = models.CharField(max_length = 20)
	email = models.CharField(max_length = 60)
	pagina_web = models.CharField(blank = True, max_length = 140)
	logo = models.ImageField(blank = True, upload_to = "static/images/logosClientes")
	usuario = models.OneToOneField(User, blank = True, null=True, on_delete = models.CASCADE )
	position = GeopositionField(blank = True)

	def __str__(self):
		return self.nombre

class Proveedores(models.Model):
	class Meta:
		verbose_name="Proveedor"
		verbose_name_plural = "Proveedores"

	id = models.AutoField(primary_key = True)
	codigo = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	direccion = models.CharField(blank=True, max_length=100)
	telefono = models.CharField(blank=True, max_length=12)
	pagina_web = models.CharField(blank=True, max_length=100)
	facebook = models.CharField(blank=True, max_length=100)
	twitter = models.CharField(blank=True, max_length=100)
	fecha_registro = models.DateField(default=datetime.datetime.today)
	position = GeopositionField(blank = True)

	def __str__(self):
		return self.nombre

class Contactos_Clientes(models.Model):
	class Meta:
		verbose_name_plural = "Contactos del Cliente"

	id = models.AutoField(primary_key = True)
	cliente = models.ForeignKey(Clientes)
	nombre = models.CharField(max_length=100)
	puesto = models.CharField(blank=True, max_length=100)
	telefono_oficina = models.CharField(blank=True, max_length=12)
	extension = models.IntegerField(blank=True, null=True)
	celular = models.CharField(blank=True, max_length=12)
	email = models.EmailField(blank = True)
	fecha_alta = models.DateField(default=datetime.datetime.today)

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

	def __str__(self):
		return self.nombre

class Planos_Clientes(models.Model):
	class Meta:
		verbose_name="Plano de Cliente"
		verbose_name_plural="Planos de Clientes"

	id = models.AutoField(primary_key=True)
	cliente = models.ForeignKey(Clientes, blank=True)
	nombre = models.CharField(blank=True, max_length=100)
	plano = models.FileField(upload_to='static/files/planos', blank=True)

	def __str__(self):
		return self.nombre
