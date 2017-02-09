from django.contrib import admin
from django.utils.html import format_html
from .models import Areas, Extintores

# Register your models here.
class AreasAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre')

class ExtintoresAdmin(admin.ModelAdmin):
	list_display = ('no_control', 'cliente', 'area', 'tipo_extintor', 'foto_extintor')

	def foto_extintor(self, obj):
		url = obj.foto.url
		return format_html("<img class='img-circle' src='/"+url+"' width=100>")

admin.site.register(Extintores, ExtintoresAdmin)
admin.site.register(Areas, AreasAdmin)