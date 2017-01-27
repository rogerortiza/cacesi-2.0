from django.contrib import admin
from django.utils.html import format_html
from .models import Empleados

# Register your models here.
class EmpleadosAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellidos', 'email', 'foto_empleado')

	def foto_empleado(self, obj):
		url = obj.foto.url
		return format_html("<img class='img-circle' src='/"+url+"' width=100>")

admin.site.register(Empleados, EmpleadosAdmin)