from django.db import models

# Create your models here.
class Areas(models.Model):
    class Meta:
        verbose_name = "Area"
        verbose_name_plural="Areas"

    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 140)

    def __str__(self):
        return self.nombre

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
