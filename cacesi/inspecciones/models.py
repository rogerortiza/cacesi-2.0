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
	status = models.CharField(max_length = 140, choices=STATUS)
	etiqueta = models.BooleanField(default =  True )
	condicion_etiqueta = models.TextField(blank = True)
	foto_etiqueta_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/etiqueta", blank = True)
	acciones_etiqueta = models.TextField(blank = True)
	foto_etiqueta_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/etiqueta", blank = True)
	arreglo_etiqueta_sitio = models.BooleanField(blank = True)
	motivos_etiqueta = models.TextField(blank = True)
	seguro = models.BooleanField(default = True)
	condicion_seguro = models.TextField(blank = True)
	foto_seguro_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/seguro", blank = True)
	acciones_seguro = models.TextField(blank = True)
	foto_seguro_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/seguro", blank = True)
	arreglo_seguro_sitio = models.BooleanField(blank = True)
	motivos_seguro = models.TextField(blank = True)
	pintura = models.BooleanField(default = True)
	condicion_pintura = models.TextField(blank = True)
	foto_pintura_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/pintura", blank = True)
	acciones_pintura = models.TextField(blank = True)
	foto_pintura_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/pintura", blank = True)
	arreglo_pintura_sitio = models.BooleanField(blank = True)
	motivos_pintura = models.TextField(blank = True)
	valvula = models.BooleanField(default = True)
	condicion_valvula = models.TextField(blank = True)
	foto_valvula_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/valvula", blank = True)
	acciones_valvula = models.TextField(blank = True)
	foto_valvula_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/valvula", blank = True)
	arreglo_valvula_sitio = models.BooleanField(blank = True)
	motivos_valvula = models.TextField(blank = True)
	nanometro = models.BooleanField(default = True)
	condicion_nanometro = models.TextField(blank = True)
	foto_nanometro_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/nanometro", blank = True)
	acciones_nanometro = models.TextField(blank = True)
	foto_nanometro_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/nanometro", blank = True)
	arreglo_nanometro_sitio = models.BooleanField(blank = True)
	motivos_nanometro = models.TextField(blank = True)
	peso = models.BooleanField(default = True)
	condicion_peso = models.TextField(blank = True)
	foto_peso_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/peso", blank = True)
	acciones_peso = models.TextField(blank = True)
	foto_peso_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/peso", blank = True)
	arreglo_peso_sitio = models.BooleanField(blank = True)
	motivos_peso = models.TextField(blank = True)
	manguera = models.BooleanField(default = True)
	condicion_manguera = models.TextField(blank = True)
	foto_manguera_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/manguera", blank = True)
	acciones_manguera = models.TextField(blank = True)
	foto_manguera_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/manguera", blank = True)
	arreglo_manguera_sitio = models.BooleanField(blank = True)
	motivos_manguera = models.TextField(blank = True)
	senalamiento = models.BooleanField(default = True)
	condicion_senalamiento = models.TextField(blank = True)
	foto_senalamiento_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/senalamiento", blank = True)
	acciones_senalamiento = models.TextField(blank = True)
	foto_senalamiento_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/senalamiento", blank = True)
	arreglo_senalamiento_sitio = models.BooleanField(blank = True)
	motivos_senalamiento = models.TextField(blank = True)
	altura = models.BooleanField(default = True)
	condicion_altura = models.TextField(blank = True)
	foto_altura_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/altura", blank = True)
	acciones_altura = models.TextField(blank = True)
	foto_altura_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/altura", blank = True)
	arreglo_altura_sitio = models.BooleanField(blank = True)
	motivos_altura = models.TextField(blank = True)
	proteccion = models.BooleanField(default = True)
	condicion_proteccion = models.TextField(blank = True)
	foto_proteccion_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/proteccion", blank = True)
	acciones_proteccion = models.TextField(blank = True)
	foto_proteccion_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/proteccion", blank = True)
	arreglo_proteccion_sitio = models.BooleanField(blank = True)
	motivos_proteccion = models.TextField(blank = True)
	limpieza = models.BooleanField(default = True)
	condicion_limpieza = models.TextField(blank = True)
	foto_limpieza_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/limpieza", blank = True)
	acciones_limpieza = models.TextField(blank = True)
	foto_limpieza_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/limpieza", blank = True)
	arreglo_limpieza_sitio = models.BooleanField(blank = True)
	motivos_limpieza = models.TextField(blank = True)
	operable = models.BooleanField(default = True)
	condicion_operable = models.TextField(blank = True)
	foto_operable_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/operable", blank = True)
	acciones_operable = models.TextField(blank = True)
	foto_operable_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/operable", blank = True)
	arreglo_operable_sitio = models.BooleanField(blank = True)
	motivos_operable = models.TextField(blank = True)
	obstruido = models.BooleanField(default = True)
	condicion_obstruido = models.TextField(blank = True)
	foto_obstruido_antes = models.ImageField(upload_to = "static/images/inspecciones/reportes/antes/obstruido", blank = True)
	acciones_obstruido = models.TextField(blank = True)
	foto_obstruido_despues = models.ImageField(upload_to = "static/images/inspecciones/reportes/despues/obstruido", blank = True)
	arreglo_obstruido_sitio = models.BooleanField(blank = True)
	motivos_obstruido = models.TextField(blank = True)
	observaciones = models.TextField()
	ultima_reca = models.DateField("Ultima Recarga")
	vencimiento = models.DateField(default = timezone.now)
	foto = models.ImageField(upload_to="static/images/inspecciones/observaciones", blank = True)

	def __str__(self):
		return str(self.extintor)

