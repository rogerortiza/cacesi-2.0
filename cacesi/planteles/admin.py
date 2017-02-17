from django.contrib import admin
from .models import Areas

# Register your models here.
class AreasAdmin(admin.ModelAdmin):
	list_display = ('id', 'cliente', 'nombre')

admin.site.register(Areas, AreasAdmin)