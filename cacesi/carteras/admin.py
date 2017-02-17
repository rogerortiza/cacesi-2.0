from django.contrib import admin
from .models import Clientes

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'email')

admin.site.register(Clientes, ClientesAdmin)
