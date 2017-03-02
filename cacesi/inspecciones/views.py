from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, View
from .models import Asignaciones, Extintores
from .forms import LoginEmpleadoForm, NewInspeccionExtintorForm

# Create your views here.
class LoginClass(View):
	form = LoginEmpleadoForm()
	message = None
	template = 'inspecciones/login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('inspecciones:new')
		return render(request, self.template, self.get_context() )

	def post(self, request, *args, **kwargs):
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate( username = username_post , password = password_post)
		if user is not None:
			try:
				me = User.objects.get(username = user)
				perfil = me.empleados.perfil
			except:
				logout_django(request)
				return redirect('inspecciones:login')
			else:
				login_django( request, user)
				return redirect('inspecciones:new')
		else:
			self.message = "Username o password incorrectos"
		return render(request, self.template, self.get_context() )

	def get_context(self):
		return {'form': self.form, 'message' : self.message}

class CreateInspeccionExtintor(LoginRequiredMixin, CreateView):
	login_url = 'inspecciones:login'
	success_url =  reverse_lazy('inspecciones:new')
	template_name = 'inspecciones/new.html'
	model = Extintores
	form_class = NewInspeccionExtintorForm

	def get_form_kwargs(self, **kwargs):
		form_kwargs = super(CreateInspeccionExtintor, self).get_form_kwargs(**kwargs)
		form_kwargs['user'] =  self.request.user
		return form_kwargs

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.empleado_id = self.request.user.empleados.id
		self.object.save()
		return HttpResponseRedirect( self.get_success_url() ) 

@login_required( login_url = 'inspecciones:login' )
def logout(request):
	logout_django(request)
	return redirect('inspecciones:login')