from django.conf.urls import url
from .views import CreateInspeccionExtintor


app_name = "inspecciones"

urlpatterns = [
    url(r'^$', CreateInspeccionExtintor.as_view(), name="new" ),
]
