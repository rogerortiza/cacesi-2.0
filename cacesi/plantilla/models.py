from django.db import models

# Create your models here.
class Empleados(models.Model):
	class Meta:
		verbose_name_plural='Empleados'

	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 140)
	apellidos = models.CharField(max_length = 140)
	edad = models.IntegerField()
	direccion = models.CharField(max_length = 140)
	ciudad = models.CharField(max_length = 140)
	estado = models.CharField(max_length = 140)
	cp = models.IntegerField()
	telefono =models.CharField(max_length = 10)
	celular = models.CharField(max_length = 10)
	email = models.EmailField()
	fecha_alta = models.DateTimeField()
	foto = models.ImageField(upload_to = "static/images/team")

	def __str__(self):
		return self.nombre+' '+self.apellidos