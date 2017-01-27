from django.db import models
from django.utils import timezone
from inventario_terceros.models import Extintores
from plantilla.models  import Empleados

# Create your models here.
class Extintores(models.Model):
	class Meta:
		verbose_name_plural='Extintores'

	id = models.AutoField(primary_key = True)
	empleado = models.ForeignKey(Empleados, on_delete = models.CASCADE)
	extintor= models.ForeignKey(Extintores, on_delete = models.CASCADE)
	fecha_revision = models.DateTimeField(default = timezone.now)
	etiqueta = models.BooleanField()
	seguro = models.BooleanField()
	pintura = models.BooleanField()
	valvula = models.BooleanField()
	nanometro = models.BooleanField()
	peso = models.BooleanField()
	manguera = models.BooleanField()
	señalamiento = models.BooleanField()
	altura = models.BooleanField()
	proteccion = models.BooleanField()
	operable = models.BooleanField()
	obstruido = models.BooleanField()
	observaciones = models.TextField()
	ultima_reca = models.DateTimeField("Ultima Recarga")
	vencimiento = models.DateField(default = timezone.now)

	def __str__(self):
		return str(self.extintor)

