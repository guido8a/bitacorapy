from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.conf.urls import url

urlpatterns = [
    path("acerca-de/", TemplateView.as_view(template_name="acerca.html"), name="acerca",),
    path("", TemplateView.as_view(template_name="home.html"), name="home",),
    path("perfil/", TemplateView.as_view(template_name="perfiles.html"), name="perfiles",),
    url(r"^home/$", views.Conectado.as_view(), name='login'),
    url(r"^ingreso/$", views.ingreso, name='ingreso'),
    url(r"^index/$", views.index, name='indice'),
    path("inicio/", TemplateView.as_view(template_name="inicio.html"), name="inicio",),
    url(r"^salir", views.salir, name='salir'),
    path("base/", TemplateView.as_view(template_name="busquedaBase.html"), name="base",),
    url(r"^buscar", views.buscar, name='buscar'),
    url(r"^ver_base", views.ver_base, name='ver_base'),
    # url(r'^item/(?P<pk>\d+)/update/$', views.itemActualizar, name='item_actualizar'),
    url(r"^actualizar/", views.itemActualizar, name='item_actualizar'),
    url(r"^actualizar/id=(?P<pk>\d+)", views.itemActualizar, name='item_actualizar'),
    url(r'^guardar/id=(?P<pk>\d+)', views.guardar_base, name='item_guardar'),
]