import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Empleados(models.Model):
	PERFILES = (
			(1, 'Inspector'),
			(2, 'Supervisor'),
			(3, 'Capacitador')
		)

	class Meta:
		verbose_name_plural='Empleados'

	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 140)
	apellidos = models.CharField(max_length = 140)
	edad = models.IntegerField()
	direccion = models.CharField(max_length = 140)
	ciudad = models.CharField(max_length = 140)
	estado = models.CharField(max_length = 140, default="Durango")
	cp = models.IntegerField()
	telefono =models.CharField(max_length = 10, blank=True)
	celular = models.CharField(max_length = 10)
	email = models.EmailField()
	fecha_alta = models.DateTimeField(default=timezone.now)
	foto = models.ImageField(upload_to = "static/images/team")
	usuario = models.OneToOneField(User, blank = True, null=True, on_delete = models.CASCADE )
	perfil =  models.IntegerField(choices = PERFILES)

	def __str__(self):
		return self.nombre+' '+self.apellidos
