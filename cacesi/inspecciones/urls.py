from django.conf.urls import url
from .views import LoginClass, logout, CreateInspeccionExtintor


app_name = "inspecciones"

urlpatterns = [
    url(r'^$', CreateInspeccionExtintor.as_view(), name="new" ),
    url(r'login/$', LoginClass.as_view(), name="login" ),
    url(r'logout/$', logout, name="logout" ),
]
