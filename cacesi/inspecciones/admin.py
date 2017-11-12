from django.contrib import admin
from .models import Asignaciones, Extintores

# Register your models here.
class AsignacionesAdmin(admin.ModelAdmin):
	list_display = ('id', 'empleado', 'mes')

class ExtintoresAdmin(admin.ModelAdmin):
	fieldsets = (
			(None, {'fields' : ('empleado', 'extintor', 'status')}),
			('Etiqueta', {
				'fields' : ('etiqueta', 'condicion_etiqueta', 'foto_etiqueta_antes', 'acciones_etiqueta', 'foto_etiqueta_despues', 'arreglo_etiqueta_sitio', 'motivos_etiqueta')}),
			('Seguro', {
				'fields' : ('seguro', 'condicion_seguro', 'foto_seguro_antes', 'acciones_seguro', 'foto_seguro_despues', 'arreglo_seguro_sitio', 'motivos_seguro')}),
			('Pintura', {
				'fields' : ('pintura', 'condicion_pintura', 'foto_pintura_antes', 'acciones_pintura', 'foto_pintura_despues', 'arreglo_pintura_sitio', 'motivos_pintura')}),
			('Valvula', {
				'fields' : ('valvula', 'condicion_valvula', 'foto_valvula_antes', 'acciones_valvula', 'foto_valvula_despues', 'arreglo_valvula_sitio', 'motivos_valvula')}),
			('Nanometro', {
				'fields' : ('nanometro', 'condicion_nanometro', 'foto_nanometro_antes', 'acciones_nanometro', 'foto_nanometro_despues', 'arreglo_nanometro_sitio', 'motivos_nanometro')}),
			('Peso', {
				'fields' : ('peso', 'condicion_peso', 'foto_peso_antes', 'acciones_peso', 'foto_peso_despues', 'arreglo_peso_sitio', 'motivos_peso')}),
			('manguera', {
				'fields' : ('manguera', 'condicion_manguera', 'foto_manguera_antes', 'acciones_manguera', 'foto_manguera_despues', 'arreglo_manguera_sitio', 'motivos_manguera')}),
			('senalamiento', {
				'fields' : ('senalamiento', 'condicion_senalamiento', 'foto_senalamiento_antes', 'acciones_senalamiento', 'foto_senalamiento_despues', 'arreglo_senalamiento_sitio', 'motivos_senalamiento')}),
			('altura', {
				'fields' : ('altura', 'condicion_altura', 'foto_altura_antes', 'acciones_altura', 'foto_altura_despues', 'arreglo_altura_sitio', 'motivos_altura')}),
			('proteccion', {
				'fields' : ('proteccion', 'condicion_proteccion', 'foto_proteccion_antes', 'acciones_proteccion', 'foto_proteccion_despues', 'arreglo_proteccion_sitio', 'motivos_proteccion')}),
			('limpieza', {
				'fields' : ('limpieza', 'condicion_limpieza', 'foto_limpieza_antes', 'acciones_limpieza', 'foto_limpieza_despues', 'arreglo_limpieza_sitio', 'motivos_limpieza')}),
			('operable', {
				'fields' : ('operable', 'condicion_operable', 'foto_operable_antes', 'acciones_operable', 'foto_operable_despues', 'arreglo_operable_sitio', 'motivos_operable')}),
			('obstruido', {
				'fields' : ('obstruido', 'condicion_obstruido', 'foto_obstruido_antes', 'acciones_obstruido', 'foto_obstruido_despues', 'arreglo_obstruido_sitio', 'motivos_obstruido')}),
			('Final', {
				'fields': ('observaciones', 'foto')})
		)

	list_display = ('id', 'extintor', 'cliente', 'area', 'empleado', 'fecha_revision')

	def area(self, obj):
		return obj.extintor.area

	def cliente(self, obj):
		return obj.extintor.cliente

admin.site.register(Asignaciones, AsignacionesAdmin)
admin.site.register(Extintores, ExtintoresAdmin)
