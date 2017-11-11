from django.contrib import admin
from .models import Clientes, Contactos_Proveedores, Proveedores

# Register your models here.
class Contactos_ProveedoresInline(admin.TabularInline):
    model = Contactos_Proveedores
    can_delete = False

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'email')

@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'giro', 'telefono')
	inlines = [Contactos_ProveedoresInline,]
