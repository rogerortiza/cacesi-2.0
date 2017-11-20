from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.views import LoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import LoginClientForm

# Create your views here.
class LoginClass(View):
	form = LoginClientForm()
	message = None
	template = 'dashboard/login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('dashboard:home')
		return render(request, self.template, self.get_context() )

	def post(self, request, *args, **kwargs):
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate( username = username_post , password = password_post)
		if user is not None:
			login_django( request, user)
			return redirect('dashboard:home')
		else:
			self.message = "Username o password incorrectos"
		return render(request, self.template, self.get_context() )

	def get_context(self):
		return {'form': self.form, 'message' : self.message}

class AreasClass(LoginRequiredMixin, View):
	login_url = 'dashboard:login'
	def get(self, request, *args, **kwargs):
		return render( request, 'dashboard/areas.html', {})

class DashboardClass(LoginRequiredMixin, View):
	login_url = 'dashboard:login'
	def get(self, request, *args, **kwargs):
		try:
			rfc = self.request.user.clientes.rfc
		except:
			logout_django(request)
			return redirect('dashboard:login')
		else:
			data = {'noExtintores' : 40}
			return render( request, 'dashboard/index.html', data)


class ExtintoresClass(LoginRequiredMixin, View):
	login_url = 'dashboard:login'
	def get(self, request, *args, **kwargs):
		return render( request, 'dashboard/extintores.html', {})

class ReportesClass(LoginRequiredMixin, View):
	login_url = 'dashboard:login'
	def get(self, request, *args, **kwargs):
		return render( request, 'dashboard/reportes.html', {})

class FacebookLogin(SocialLoginView):
	adapter_class = FacebookOAuth2Adapter

class TwitterLogin(LoginView):
	serializer_class = TwitterLoginSerializer
	adapter_class = TwitterOAuthAdapter

@login_required( login_url = 'dashboard:login' )
def logout(request):
	logout_django(request)
	return redirect('dashboard:login')

def home(request):
	return render( request, 'index.html', {})

def asesorias(request):
	return render( request, 'home/asesorias.html', {})

#def dashboard(request):
#	return render( request, 'dashboard/index.html', {})

def team(request):
	return render( request, 'home/team.html', {})
