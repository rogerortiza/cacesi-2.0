from django.db import models
from carteras.models import Clientes

# Create your models here.
class Areas(models.Model):
    class Meta:
        verbose_name = "Area"
        verbose_name_plural="Areas"
        unique_together = ("cliente", "nombre")

    id = models.AutoField(primary_key = True)
    cliente = models.ForeignKey(Clientes)
    nombre = models.CharField(max_length = 140)
    responsable = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre+" - "+self.cliente.nombre

class CategoriaProductos(models.Model):
    class Meta:
        verbose_name="Categoria de Producto"
        verbose_name_plural = "Categorias de Productos"

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class GiroProveedores(models.Model):
    class Meta:
        verbose_name = "Giro"
        verbose_name_plural = "Giro de Proveedores"

    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
