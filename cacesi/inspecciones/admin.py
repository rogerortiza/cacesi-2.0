from django.contrib import admin
from .models import Extintores

# Register your models here.
class ExtintoresAdmin(admin.ModelAdmin):
	list_display = ('extintor', 'cliente', 'empleado', 'fecha_revision')

	def cliente(self, obj):
		return obj.extintor.cliente

admin.site.register(Extintores, ExtintoresAdmin)
