from django.contrib import admin
from .models import Clientes, Contactos_Clientes, Contactos_Proveedores, Proveedores

# Register your models here.
class Contactos_ClientesInline(admin.TabularInline):
    model = Contactos_Clientes
    can_delete = False

class Contactos_ProveedoresInline(admin.TabularInline):
    model = Contactos_Proveedores
    can_delete = False

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email')
    list_display_links = ('nombre',)
    exclude = ('fecha_alta',)
    inlines = [Contactos_ClientesInline,]

@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'giro', 'telefono')
    list_display_links = ('nombre',)
    exclude = ('fecha_registro',)
    inlines = [Contactos_ProveedoresInline,]
