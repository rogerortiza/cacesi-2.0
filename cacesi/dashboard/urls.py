from django.conf.urls import url
from .views import AreasClass, DashboardClass, ExtintoresClass, LoginClass, logout, ReportesClass

app_name = "dashboard"

urlpatterns = [
    url(r'^$', DashboardClass.as_view(), name="home" ),
    url(r'^login/$', LoginClass.as_view(), name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^areas/$', AreasClass.as_view(), name = 'areas'),
    url(r'^extintores/$', ExtintoresClass.as_view(), name = 'extintores'),
    url(r'^reportes/$', ReportesClass.as_view(), name = 'reportes'),
]
