from django.conf.urls import url
from .views import asesorias, home, equipo


urlpatterns = [
    url(r'^asesorias/', asesorias, name="asesorias"),
    url(r'^equipo/', equipo, name="equipo"),
]
