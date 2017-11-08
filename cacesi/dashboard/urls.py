from django.conf.urls import url
from .views import AreasClass, DashboardClass, ExtintoresClass, LoginClass, logout, ReportesClass
from django.views.generic import View, TemplateView

app_name = "dashboard"

urlpatterns = [
    url(r'^$', DashboardClass.as_view(), name="home" ),
    url(r'^login/$', LoginClass.as_view(), name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^areas/$', TemplateView.as_view(template_name="dashboard/views/areas.html"), name = 'areas'),
    url(r'^extintores/$', TemplateView.as_view(template_name="dashboard/views/extintores.html"), name = 'extintores'),
    url(r'^reportes/$', ReportesClass.as_view(), name = 'reportes'),
    url(r'^inspextintores/$', TemplateView.as_view(template_name="dashboard/views/inspeccion_extintores.html")),
]
