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
    # username = request.GET.get('username', None)
    # pswd = request.GET.get('pswd', None)
    # print('inicio de ingreso ' + username)
    print(request)
    username = request.POST.get('login', None)
    pswd = request.POST.get('pass', None)
    print('inicio de ingreso {}'.format(username))

    usuario = User.objects.filter(username__iexact=username).only('username','password')
    user = auth.authenticate(request, username=username, password=pswd)
    print("autenticado: {}".format(user))
    if(user):
        data = {
            'resp': 'ok',
        }
        request.session['usro'] = username
        prfl = Perfil.objects.all()
        print("--> {} {}".format(prfl[0].id, prfl[0].descripcion))
        # return redirect('/perfil', {'perfiles': prfl})
        return render(request, 'perfiles.html', {'perfiles': prfl})
    else:
        data = {
            'resp': 'no',
        }
        return redirect('/')
    print(data)
    # response = redirect('/perfil/')
    # return response
    # return JsonResponse(data)

def index(request):
    print(request)
    prfl = request.POST.get('perfil', None)
    print('inicio de {} perfil {}'.format(request.session['usro'], prfl))
    print('session: {}'.format(request.session))

    if(prfl):
        request.session['prfl'] = prfl
        # return redirect('/perfil', {'perfiles': prfl})
        return render(request, 'inicio.html')
    else:
        return redirect('/', {'perfiles': Perfil.objects.all()})

def salir(request):
    print(request)
    request.session.clear()
    return redirect('/')

