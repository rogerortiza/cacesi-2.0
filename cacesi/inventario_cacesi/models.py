import datetime
from django.db import models
from carteras.models import Proveedores

# Create your models here.
class Productos(models.Model):
    class Meta:
        verbose_name_plural = "Productos"

    id = models.AutoField(primary_key = True)
    clave = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(blank=True, null=True, max_length=100, verbose_name="Unidad de Medida")
    proveedor = models.ForeignKey(Proveedores)
    precio_proveedor = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    precio_publico = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    stock_maximo = models.IntegerField(blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)
    existencia = models.IntegerField(blank=True, null=True)
    exposicion = models.IntegerField(blank=True, null=True)
    fecha_alta = models.DateField(default=datetime.datetime.today)
