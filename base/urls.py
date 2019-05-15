from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf.urls import url

urlpatterns = [
    path("acerca-de/", TemplateView.as_view(template_name="acerca.html"), name="acerca",),
    path("", TemplateView.as_view(template_name="home.html"), name="home",),
    path("perfil/", TemplateView.as_view(template_name="perfiles.html"), name="perfiles",),
    url(r"^home/$", views.Conectado.as_view(), name='login'),
    url(r"^ingreso/$", views.ingreso, name='ingreso'),
]