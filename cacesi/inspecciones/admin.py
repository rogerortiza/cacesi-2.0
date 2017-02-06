from django.contrib import admin
from .models import Extintores

# Register your models here.
class ExtintoresAdmin(admin.ModelAdmin):
	list_display = ('extintor', 'cliente', 'area', 'empleado', 'fecha_revision')

	def area(self, obj):
		return obj.extintor.area

	def cliente(self, obj):
		return obj.extintor.cliente

admin.site.register(Extintores, ExtintoresAdmin)
