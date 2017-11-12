from django.db import models
from django.utils import timezone
from carteras.models import Clientes
from catalogos.models import Areas

# Create your models here.
class Extintores(models.Model):
	CAPACIDAD = [
		('Kg', 'Kilogramos'),
		('Lts', 'Litros'),
	]

	CLASIFICACION_EXTINTORES = [
		('Automotriz', 'Automotriz'),
		('Movil', 'Movil'),
		('Poratil', 'Portatil')
	]

	MEDIDADAS_CONTENIDO = [
		('3/4', '3/4'),
		('1', '1'),
		('2', '2'),
		('2.5', '2.5'),
		('4.5', '4.5'),
		('6', '6'),
		('6.8', '6.8'),
		('9', '9'),
		('10', '10'),
		('12', '12'),
		('22', '22'),
		('34', '34'),
		('45', '45'),
		('50', '50'),
		('68', '68')
	]

	TIPOS_EXTINTORES = [
		('AGUA', 'AGUA'),
		('AGUA CON ESPUMA', 'AGUA CON ESPUMA'),
		('Co2', 'Co2'),
		('CLASE D', 'CLASE D'),
		('CLASE K', 'CLASE K'),
		('HALOTRON', 'HALOTRON'),
		('PQS', 'PQS')
	]

	class Meta:
		verbose_name='Extintor'
		verbose_name_plural='Extintores'

	id = models.AutoField(primary_key = True)
	cliente = models.ForeignKey(Clientes)
	area = models.ForeignKey(Areas)
	ubicacion = models.CharField(max_length = 140)
	no_control = models.CharField(max_length = 140)
	tipo_extintor = models.CharField(max_length = 140, choices = TIPOS_EXTINTORES)
	clasificacion = models.CharField(max_length = 140, choices = CLASIFICACION_EXTINTORES)
	capacidad = models.CharField(max_length = 140, choices = CAPACIDAD)
	contenido_neto = models.CharField(max_length=100, choices = MEDIDADAS_CONTENIDO)
	ultima_reca = models.DateField("Ultima Recarga", default = timezone.now)
	vencimiento = models.DateField()
	foto = models.ImageField(upload_to="static/images/extintores", blank=True)

	def save(self, *args, **kwargs):
		self.vencimiento = self.ultima_reca.replace(timezone.now().year + 1)
		super(Extintores, self).save(*args, **kwargs)

	def __str__(self):
		return self.no_control
