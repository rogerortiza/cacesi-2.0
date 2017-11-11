from django.contrib import admin
from django.utils.html import format_html
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
    list_display = ('id', 'modelo', 'nombre', 'categoria', 'proveedor', 'precio_proveedor', 'en_existencia')
    list_filter = ('proveedor','categoria',)
    search_fields = ('nombre', 'clave',)
    resource_class = ProductosResource

    def en_existencia(self, obj):
        stockMaximo = obj.stock_maximo
        stockMinimo = round(stockMaximo*.25)
        styleUntis = "style='background-color:greenyellow;" if obj.existencia > stockMinimo else "style='background-color:red;color:white;"
        return format_html("<div "+styleUntis+"display:inline-block;width:25px;text-align:center;'>"+str(obj.existencia)+"</div>")
    """
        def foto(self, obj):
            url = obj.avatar.url
            return format_html("<img class='img-circle' src='/"+url+"' width=70>")
    """
