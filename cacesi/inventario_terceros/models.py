from django.db import models
from carteras.models import Clientes

# Create your models here.
class Areas(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 140)
	telefono = models.CharField(max_length = 10)

	def __str__(self):
		return self.nombre

class Extintores(models.Model):
	class Meta:
		verbose_name_plural='Extintores'

	id = models.AutoField(primary_key = True)
	cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)
	area =  models.ForeignKey(Areas, on_delete = models.CASCADE)
	ubicacion = models.CharField(max_length = 140)
	no_control = models.CharField(max_length = 140)
	tipo_extintor = models.CharField(max_length = 140)
	clasificacion = models.CharField(max_length = 140)
	capacidad = models.CharField(max_length = 140)
	foto = models.ImageField(upload_to="static/images/extintores")

	def __str__(self):
		return self.no_control