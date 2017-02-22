"""cacesi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers
from dashboard.views import asesorias, DashboardClass, LoginClass, home, team
from carteras.viewsets import  ClientesViewSet
from inspecciones.viewsets import ExtintoresViewSet
from inventario_terceros.viewsets import ExtintoresTercerosViewSet
from planteles.viewsets import AreasViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewSet, base_name="clientes")
router.register(r'inspecciones_extintores', ExtintoresViewSet, base_name="inspecciones_extintores")
router.register(r'extintores_terceros', ExtintoresTercerosViewSet, base_name="exintores_terceros")

dashboard_router = routers.NestedSimpleRouter(router, r'clientes', lookup='cliente')
dashboard_router.register(r'areas', AreasViewSet, base_name='areas')
dashboard_router.register(r'extintores_terceros', ExtintoresTercerosViewSet, base_name='exintores_terceros')
dashboard_router.register(r'inspeccion_extintores', ExtintoresViewSet, base_name='inspeccion_extintores')


urlpatterns = [
	url(r'^$', home, name="home" ),
	url(r'^asesorias/$', asesorias, name="asesorias" ),
	url(r'^dashboard/', include('dashboard.urls')),
    url(r'^inspecciones/', include('inspecciones.urls')),
    url(r'^team/$', team, name="team" ),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(dashboard_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    #url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
]
