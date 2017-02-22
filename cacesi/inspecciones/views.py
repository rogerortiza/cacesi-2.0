from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from .models import Extintores
from .forms import NewInspeccionExtintorForm

# Create your views here.
class CreateInspeccionExtintor(CreateView):
	success_url =  reverse_lazy('inspecciones:new')
	template_name = 'inspecciones/new.html'
	model = Extintores
	form_class = NewInspeccionExtintorForm