from django.contrib import admin
from .models import Areas, CategoriaProductos, GiroProveedores

# Register your models here.
@admin.register(Areas)
class AreasAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoriaProductos)
class CategoriaProductosAdmin(admin.ModelAdmin):
    pass

@admin.register(GiroProveedores)
class GiroProveedoresAdmin(admin.ModelAdmin):
    pass
