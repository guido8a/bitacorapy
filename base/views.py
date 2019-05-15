from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Perfil
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib import auth


class Conectado(CreateView):
    print("crea home..")
    template_name = 'home.html'
    form_class = UserCreationForm

def ingreso(request):
    username = request.GET.get('username', None)
    pswd = request.GET.get('pswd', None)
    print('inicio de ingreso ' + username)
    usuario = User.objects.filter(username__iexact=username).only('username','password')
    user = auth.authenticate(request, username=username, password=pswd)
    print(user)
    if(user):
        data = {
            'resp': 'ok',
        }
    else:
        data = {
            'resp': 'no',
        }
    # return redirect('/perfil', {'perfiles': Perfil.objects.all()})
    print(data)
    # response = redirect('/perfil/')
    # return response
    return JsonResponse(data)

