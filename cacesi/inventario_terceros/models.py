from django.db import models
from carteras.models import Clientes
from planteles.models import Areas

# Create your models here.
class Extintores(models.Model):
	CAPACIDAD = [
		('2.5', '2.5'),
		('4.5', '4.5'),
		('6', '6'),
		('9', '9'),
		('34', '34'),
		('50', '50')
	]

	TIPOS_EXTINTORES = [
		('CO2', 'CO2'),
		('PQS', 'PQS'),
		('TIPO K', 'TIPO K')
	]

	class Meta:
		verbose_name_plural='Extintores'

	id = models.AutoField(primary_key = True)
	cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)
	area =  models.ForeignKey(Areas, on_delete = models.CASCADE)
	ubicacion = models.CharField(max_length = 140)
	no_control = models.CharField(max_length = 140)
	tipo_extintor = models.CharField(max_length = 140, choices = TIPOS_EXTINTORES)
	clasificacion = models.CharField(max_length = 140)
	capacidad = models.CharField(max_length = 140, choices = CAPACIDAD)
	foto = models.ImageField(upload_to="static/images/extintores")

	def __str__(self):
		return self.no_control