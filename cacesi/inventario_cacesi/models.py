import datetime
from django.db import models
from carteras.models import Proveedores

# Create your models here.
class Productos(models.Model):
    class Meta:
        verbose_name_plural = "Productos"

    CATEGORIA_PRODUCTO = {
        ('1', 'Proteccion Para la Cabeza'),
        ('2', 'Proteccion Ocular'),
        ('3', 'Proteccion Respiratoria')
    }

    id = models.AutoField(primary_key = True)
    clave = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(blank=True, max_length=100, choices=CATEGORIA_PRODUCTO)
    unidad_medida = models.CharField(blank=True, null=True, max_length=100, verbose_name="Unidad de Medida")
    proveedor = models.ForeignKey(Proveedores)
    precio_proveedor = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    precio_publico = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    stock_maximo = models.IntegerField(blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)
    existencia = models.IntegerField(blank=True, null=True)
    exposicion = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(blank = True, upload_to="static/images/productos")
    fecha_alta = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.nombre
