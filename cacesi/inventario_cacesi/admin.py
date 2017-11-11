from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Productos

# Register your models here.
class ProductosResource(resources.ModelResource):
    class Meta:
        model = Productos
        skip_unchanged = True
        report_skipped = False

@admin.register(Productos)
class ProductosAdmin(ImportExportModelAdmin):
    list_display = ('id', 'modelo', 'nombre', 'categoria', 'proveedor', 'precio_proveedor', 'existencia')
    list_filter = ('proveedor','categoria',)
    search_fields = ('nombre', 'clave',)
    resource_class = ProductosResource
