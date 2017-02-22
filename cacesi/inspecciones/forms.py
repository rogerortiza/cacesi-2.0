#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import Extintores
import datetime

class NewInspeccionExtintorForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(NewInspeccionExtintorForm, self).__init__(*args, **kwargs)
		self.fields['fecha_revision'].widget.attrs.update( {'class': 'datepicker' } )
		self.fields['etiqueta'].widget.attrs.update( {'id' : 'etiqueta', 'class': '', 'ng-model' : 'etiqueta', 'ng-init' : 'etiqueta = true' } )
		self.fields['condicion_etiqueta'].widget.attrs.update( {'id' : 'condicion_etiqueta', 'class': 'materialize-textarea' } )
		self.fields['acciones_etiqueta'].widget.attrs.update( {'id' : 'acciones_etiqueta', 'class': 'materialize-textarea' } )
		self.fields['arreglo_etiqueta_sitio'].widget.attrs.update( {'id' : 'arreglo_etiqueta_sitio', 'class': '', 'ng-model' : 'etiqueta_sitio', 'ng-init' : 'etiqueta_sitio = true' } )
		self.fields['motivos_etiqueta'].widget.attrs.update( {'id' : 'motivos_etiqueta', 'class': 'materialize-textarea' } )
		self.fields['seguro'].widget.attrs.update( {'id' : 'seguro', 'class': '', 'ng-model' : 'seguro', 'ng-init' : 'seguro = true' } )
		self.fields['condicion_seguro'].widget.attrs.update( {'id' : 'condicion_seguro', 'class': 'materialize-textarea' } )
		self.fields['acciones_seguro'].widget.attrs.update( {'id' : 'acciones_seguro', 'class': 'materialize-textarea' } )
		self.fields['arreglo_seguro_sitio'].widget.attrs.update( {'id' : 'arreglo_seguro_sitio', 'class': '', 'ng-model' : 'seguro_sitio', 'ng-init' : 'seguro_sitio = true' } )
		self.fields['motivos_seguro'].widget.attrs.update( {'id' : 'motivos_seguro', 'class': 'materialize-textarea' } )
		self.fields['pintura'].widget.attrs.update( {'id' : 'pintura', 'class': '', 'ng-model' : 'pintura', 'ng-init' : 'pintura = true' } )
		self.fields['condicion_pintura'].widget.attrs.update( {'id' : 'condicion_pintura', 'class': 'materialize-textarea' } )
		self.fields['acciones_pintura'].widget.attrs.update( {'id' : 'acciones_pintura', 'class': 'materialize-textarea' } )
		self.fields['arreglo_pintura_sitio'].widget.attrs.update( {'id' : 'arreglo_pintura_sitio', 'class': '', 'ng-model' : 'pintura_sitio', 'ng-init' : 'pintura_sitio = true' } )
		self.fields['motivos_pintura'].widget.attrs.update( {'id' : 'motivos_pintura', 'class': 'materialize-textarea' } )
		self.fields['valvula'].widget.attrs.update( {'id' : 'valvula', 'class': '', 'ng-model' : 'valvula', 'ng-init' : 'valvula = true' } )
		self.fields['condicion_valvula'].widget.attrs.update( {'id' : 'condicion_valvula', 'class': 'materialize-textarea' } )
		self.fields['acciones_valvula'].widget.attrs.update( {'id' : 'acciones_valvula', 'class': 'materialize-textarea' } )
		self.fields['arreglo_valvula_sitio'].widget.attrs.update( {'id' : 'arreglo_valvula_sitio', 'class': '', 'ng-model' : 'valvula_sitio', 'ng-init' : 'valvula_sitio = true' } )
		self.fields['motivos_valvula'].widget.attrs.update( {'id' : 'motivos_valvula', 'class': 'materialize-textarea' } )
		self.fields['nanometro'].widget.attrs.update( {'id' : 'nanometro', 'class': '', 'ng-model' : 'nanometro', 'ng-init' : 'nanometro = true' } )
		self.fields['condicion_nanometro'].widget.attrs.update( {'id' : 'condicion_nanometro', 'class': 'materialize-textarea' } )
		self.fields['acciones_nanometro'].widget.attrs.update( {'id' : 'acciones_nanometro', 'class': 'materialize-textarea' } )
		self.fields['arreglo_nanometro_sitio'].widget.attrs.update( {'id' : 'arreglo_nanometro_sitio', 'class': '', 'ng-model' : 'nanometro_sitio', 'ng-init' : 'nanometro_sitio = true' } )
		self.fields['motivos_nanometro'].widget.attrs.update( {'id' : 'motivos_nanometro', 'class': 'materialize-textarea' } )
		self.fields['peso'].widget.attrs.update( {'id' : 'peso', 'class': '', 'ng-model' : 'peso', 'ng-init' : 'peso = true' } )
		self.fields['condicion_peso'].widget.attrs.update( {'id' : 'condicion_peso', 'class': 'materialize-textarea' } )
		self.fields['acciones_peso'].widget.attrs.update( {'id' : 'acciones_peso', 'class': 'materialize-textarea' } )
		self.fields['arreglo_peso_sitio'].widget.attrs.update( {'id' : 'arreglo_peso_sitio', 'class': '', 'ng-model' : 'peso_sitio', 'ng-init' : 'peso_sitio = true' } )
		self.fields['motivos_peso'].widget.attrs.update( {'id' : 'motivos_peso', 'class': 'materialize-textarea' } )
		self.fields['manguera'].widget.attrs.update( {'id' : 'manguera', 'class': '', 'ng-model' : 'manguera', 'ng-init' : 'manguera = true' } )
		self.fields['condicion_manguera'].widget.attrs.update( {'id' : 'condicion_manguera', 'class': 'materialize-textarea' } )
		self.fields['acciones_manguera'].widget.attrs.update( {'id' : 'acciones_manguera', 'class': 'materialize-textarea' } )
		self.fields['arreglo_manguera_sitio'].widget.attrs.update( {'id' : 'arreglo_manguera_sitio', 'class': '', 'ng-model' : 'manguera_sitio', 'ng-init' : 'manguera_sitio = true' } )
		self.fields['motivos_manguera'].widget.attrs.update( {'id' : 'motivos_manguera', 'class': 'materialize-textarea' } )
		self.fields['senalamiento'].widget.attrs.update( {'id' : 'senalamiento', 'class': '', 'ng-model' : 'senalamiento', 'ng-init' : 'senalamiento = true' } )
		self.fields['condicion_senalamiento'].widget.attrs.update( {'id' : 'condicion_senalamiento', 'class': 'materialize-textarea' } )
		self.fields['acciones_senalamiento'].widget.attrs.update( {'id' : 'acciones_senalamiento', 'class': 'materialize-textarea' } )
		self.fields['arreglo_senalamiento_sitio'].widget.attrs.update( {'id' : 'arreglo_senalamiento_sitio', 'class': '', 'ng-model' : 'senalamiento_sitio', 'ng-init' : 'senalamiento_sitio = true' } )
		self.fields['motivos_senalamiento'].widget.attrs.update( {'id' : 'motivos_senalamiento', 'class': 'materialize-textarea' } )
		self.fields['altura'].widget.attrs.update( {'id' : 'altura', 'class': '', 'ng-model' : 'altura', 'ng-init' : 'altura = true' } )
		self.fields['condicion_altura'].widget.attrs.update( {'id' : 'condicion_altura', 'class': 'materialize-textarea' } )
		self.fields['acciones_altura'].widget.attrs.update( {'id' : 'acciones_altura', 'class': 'materialize-textarea' } )
		self.fields['arreglo_altura_sitio'].widget.attrs.update( {'id' : 'arreglo_altura_sitio', 'class': '', 'ng-model' : 'altura_sitio', 'ng-init' : 'altura_sitio = true' } )
		self.fields['motivos_altura'].widget.attrs.update( {'id' : 'motivos_altura', 'class': 'materialize-textarea' } )
		self.fields['proteccion'].widget.attrs.update( {'id' : 'proteccion', 'class': '', 'ng-model' : 'proteccion', 'ng-init' : 'proteccion = true' } )
		self.fields['condicion_proteccion'].widget.attrs.update( {'id' : 'condicion_proteccion', 'class': 'materialize-textarea' } )
		self.fields['acciones_proteccion'].widget.attrs.update( {'id' : 'acciones_proteccion', 'class': 'materialize-textarea' } )
		self.fields['arreglo_proteccion_sitio'].widget.attrs.update( {'id' : 'arreglo_proteccion_sitio', 'class': '', 'ng-model' : 'proteccion_sitio', 'ng-init' : 'proteccion_sitio = true' } )
		self.fields['motivos_proteccion'].widget.attrs.update( {'id' : 'motivos_proteccion', 'class': 'materialize-textarea' } )
		self.fields['limpieza'].widget.attrs.update( {'id' : 'limpieza', 'class': '', 'ng-model' : 'limpieza', 'ng-init' : 'limpieza = true' } )
		self.fields['condicion_limpieza'].widget.attrs.update( {'id' : 'condicion_limpieza', 'class': 'materialize-textarea' } )
		self.fields['acciones_limpieza'].widget.attrs.update( {'id' : 'acciones_limpieza', 'class': 'materialize-textarea' } )
		self.fields['arreglo_limpieza_sitio'].widget.attrs.update( {'id' : 'arreglo_limpieza_sitio', 'class': '', 'ng-model' : 'limpieza_sitio', 'ng-init' : 'limpieza_sitio = true' } )
		self.fields['motivos_limpieza'].widget.attrs.update( {'id' : 'motivos_limpieza', 'class': 'materialize-textarea' } )
		self.fields['operable'].widget.attrs.update( {'id' : 'operable', 'class': '', 'ng-model' : 'operable', 'ng-init' : 'operable = true' } )
		self.fields['condicion_operable'].widget.attrs.update( {'id' : 'condicion_operable', 'class': 'materialize-textarea' } )
		self.fields['acciones_operable'].widget.attrs.update( {'id' : 'acciones_operable', 'class': 'materialize-textarea' } )
		self.fields['arreglo_operable_sitio'].widget.attrs.update( {'id' : 'arreglo_operable_sitio', 'class': '', 'ng-model' : 'operable_sitio', 'ng-init' : 'operable_sitio = true' } )
		self.fields['motivos_operable'].widget.attrs.update( {'id' : 'motivos_operable', 'class': 'materialize-textarea' } )
		self.fields['obstruido'].widget.attrs.update( {'id' : 'obstruido', 'class': '', 'ng-model' : 'obstruido', 'ng-init' : 'obstruido = true' } )
		self.fields['condicion_obstruido'].widget.attrs.update( {'id' : 'condicion_obstruido', 'class': 'materialize-textarea' } )
		self.fields['acciones_obstruido'].widget.attrs.update( {'id' : 'acciones_obstruido', 'class': 'materialize-textarea' } )
		self.fields['arreglo_obstruido_sitio'].widget.attrs.update( {'id' : 'arreglo_obstruido_sitio', 'class': '', 'ng-model' : 'obstruido_sitio', 'ng-init' : 'obstruido_sitio = true' } )
		self.fields['motivos_obstruido'].widget.attrs.update( {'id' : 'motivos_obstruido', 'class': 'materialize-textarea' } )
		
		self.fields['observaciones'].widget.attrs.update( {'id' : 'observaciones', 'class': 'materialize-textarea' } )
		self.fields['ultima_reca'].widget.attrs.update( {'class': 'datepicker' } )
		self.fields['vencimiento'].widget.attrs.update( {'class': 'datepicker' } )


	class Meta:
		model = Extintores
		fields = ('__all__')