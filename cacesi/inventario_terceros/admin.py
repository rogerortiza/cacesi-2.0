from django.contrib import admin
from django.utils.html import format_html
from .models import Extintores

# Register your models here.
class ExtintoresAdmin(admin.ModelAdmin):
	list_display = ('no_control', 'cliente', 'tipo_extintor', 'foto_extintor')

	def foto_extintor(self, obj):
		url = obj.foto.url
		return format_html("<img class='img-circle' src='/"+url+"' width=100>")

admin.site.register(Extintores, ExtintoresAdmin)
