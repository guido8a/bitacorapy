from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Perfil
from .models import Base
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db import connection
from common import funciones
import time


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

@csrf_exempt
def buscar(request):
    start_time = time.time()
    print("buscar {}".format(request))
    print(request.POST.get('buscar', None))

    buscar = tuple(request.POST.get('buscar', None).split(' '))
    print(buscar)
    # sql = "select base__id, sum(plbrvlor) valor from plbr where plbrplbr like '%{}%' group by base__id order by 2".format(buscar[0])
    sql = "select base__id from plbr where plbrplbr like '%{}%' group by base__id order by sum(plbrvlor) desc".format(buscar[0])
    print(sql)
    # retorna = ejecuta_sql(sql)
    retorna = funciones.ejecutaSql(sql)
    data = set()
    for d in retorna:
        # print(d)
        # print("id: {}".format(d[0]))
        base = Base.objects.get(id=d[0])
        data.add(base)

    if(data):
        # print(data[0].tema.descripcion)
        resp = render_to_string('tablaBusquedaBase.html', {'data': data})
        # print("----> {}".format(len(data)))
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        return HttpResponse(resp)
    else:
        return redirect('/base')

@csrf_exempt
def ver_base(request):
    print("ver_base {}".format(request))
    base_id = request.POST.get('id', None)
    # print(base_id)

    data = set()
    # base = Base.objects.get(id = base_id)
    base = Base.objects.get(id = base_id)
    # print("--base: {}".format(base))
    if(base):
        # print("base: {}".format(base.problema))
        resp = render_to_string('show_ajax.html', {'data': base})
        # print("html: {}".format(resp))
        return HttpResponse(resp)
    else:
        return redirect('/buscar')

