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
    list_display_links = ('modelo', 'nombre',)
    list_filter = ('proveedor','categoria')
    search_fields = ('nombre', 'clave',)
    exclude = ("fecha_alta",)
    resource_class = ProductosResource

    def en_existencia(self, obj):
        stockMedio = round(obj.stock_maximo*.70)
        stockMinimo = round(obj.stock_maximo*.25)
        if obj.existencia <= stockMedio and obj.existencia > stockMinimo:
            styleUntis = "style='background-color:orange;color:white;"
        elif obj.existencia <= stockMinimo:
            styleUntis = "style='background-color:red;color:white;"
        else:
            styleUntis = "style='background-color:greenyellow;color:#000000"

        return format_html("<div "+styleUntis+"display:inline-block;width:25px;text-align:center;'>"+str(obj.existencia)+"</div>")

"""
        def foto(self, obj):
            url = obj.avatar.url
            return format_html("<img class='img-circle' src='/"+url+"' width=70>")
    """
