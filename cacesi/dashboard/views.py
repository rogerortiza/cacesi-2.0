from django.shortcuts import render

# Create your views here.
def home(request):
	return render( request, 'index.html', {})

def asesorias(request):
	return render( request, 'home/asesorias.html', {})

def team(request):
	return render( request, 'home/team.html', {})
