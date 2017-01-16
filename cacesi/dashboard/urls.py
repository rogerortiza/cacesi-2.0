from django.conf.urls import url
from .views import asesorias, home

urlpatterns = [
    url(r'^asesorias/', asesorias, name="asesorias"),
]
