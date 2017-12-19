from django.contrib import admin
from .models import Clientes, Contactos_Clientes, Contactos_Proveedores, Proveedores, Planos_Clientes

# Register your models here.
class ContactosClientesInline(admin.TabularInline):
    model = Contactos_Clientes
    can_delete = False

class ContactosProveedoresInline(admin.TabularInline):
    model = Contactos_Proveedores
    can_delete = False

class PlanosClientesInline(admin.TabularInline):
    model = Planos_Clientes
    can_delete = False

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email')
    list_display_links = ('nombre',)
    fields = (('nombre', 'sucursal'), ('razon_social', 'rfc'), ('codigo', 'giro'), ('calle', 'colonia'), ('municipio','estado'), ('pais', 'cp'), 'region', ('telefono', 'email'), ('pagina_web', 'logo'), 'usuario', 'position')
    exclude = ('fecha_alta',)
    inlines = [ContactosClientesInline, PlanosClientesInline]

@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono')
    list_display_links = ('nombre',)
    exclude = ('fecha_registro',)
    inlines = [ContactosProveedoresInline,]
