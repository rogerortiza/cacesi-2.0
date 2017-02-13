from django.db import models
from django.utils import timezone
from inventario_terceros.models import Extintores
from plantilla.models  import Empleados

# Create your models here.
class Extintores(models.Model):
	STATUS = [
		('En su lugar', 'En su lugar'),
		('No Encontrado', 'No Encontrado'),
		('Reemplazado por caducidad', 'Reemplazado por caducidad'),
		('Reemplazado por falta de presion', 'Reemplazado por falta de presion')
	]

	class Meta:
		verbose_name_plural='Extintores'

	id = models.AutoField(primary_key = True)
	empleado = models.ForeignKey(Empleados, on_delete = models.CASCADE)
	extintor= models.ForeignKey(Extintores, on_delete = models.CASCADE)
	fecha_revision = models.DateTimeField(default = timezone.now)
	condicion = models.TextField()
	foto_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes")
	acciones = models.TextField()
	status = models.CharField(max_length = 140, choices=STATUS)
	foto_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues")
	etiqueta = models.BooleanField()
	seguro = models.BooleanField()
	pintura = models.BooleanField()
	valvula = models.BooleanField()
	nanometro = models.BooleanField()
	peso = models.BooleanField()
	manguera = models.BooleanField()
	senalamiento = models.BooleanField()
	altura = models.BooleanField()
	proteccion = models.BooleanField()
	limpieza = models.BooleanField()
	operable = models.BooleanField()
	obstruido = models.BooleanField()
	observaciones = models.TextField()
	ultima_reca = models.DateTimeField("Ultima Recarga")
	vencimiento = models.DateField(default = timezone.now)
	foto = models.ImageField(upload_to="static/images/inspecciones/observaciones", blank = True)

	def __str__(self):
		return str(self.extintor)

