from django.contrib import admin
from django.utils.html import format_html
from .models import Extintores

# Register your models here.
class ExtintoresAdmin(admin.ModelAdmin):
	list_display = ('no_control', 'cliente', 'ultima_reca', 'vencimiento', 'foto_extintor')
	exclude = ('vencimiento',)

	"""def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "area":
			kwargs["queryset"] = Areas.objects.filter(area=request.user.empledos.asignaciones.area)
			return super(ExtintoresAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)"""

	def foto_extintor(self, obj):
		url = obj.foto.url
		return format_html("<img class='img-circle' src='/"+url+"' width=100>")

admin.site.register(Extintores, ExtintoresAdmin)
