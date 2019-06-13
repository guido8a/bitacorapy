from django import template

register = template.Library()

from ..models import Base
from .. import urls
from common import funciones

@register.simple_tag()
def cuenta_base():
  	return Base.objects.count()

@register.simple_tag()
def menu_mock():
  	return """
  	<nav class="navbar navbar-expand-lg navbar-dark primary-color" style="background-color: #eac57b" role="navigation">
  	<div class="container-fluid"><div class="navbar-header">
  	<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
  	<span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button>
  	<a class="navbar-brand navbar-logo" href="/bitacora/"><img src="/bitacora/images/logo.png" height="32px"/></a>
  	</div><div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1"><ul class="nav navbar-nav">
  	<li class="dropdown dropdown-item"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Inicio<b class="caret"></b></a>
  	<ul class="dropdown-menu"><li><a href="/bitacora/inicio/index">Inicio</a></li></ul></li><li class="dropdown">
  	<a href="#" class="dropdown-toggle" data-toggle="dropdown">Administración<b class="caret"></b></a><ul class="dropdown-menu menu-item">
  	<li><a href="/bitacora/acciones/acciones">Acciones</a></li><li><a href="/bitacora/buscarBase/actualizarPlbr">Actualizar Búsquedas</a></li>
  	<li><a href="/bitacora/departamento/arbol">Departamentos y usuarios</a></li>
  	<li><a href="/bitacora/diaLaborable/calendario">Días laborables</a></li>
  	<li><a href="/bitacora/parametros/list">Parámetros del sistema</a></li>
  	<li><a href="/bitacora/persona/list">Personal</a></li>
  	<li><a href="/bitacora/tema/list">Temas de la Base de conocimiento</a></li></ul></li>
  	<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Conocimiento<b class="caret"></b></a><ul class="dropdown-menu">
  	<li><a href="/bitacora/buscarBase/busquedaBase">Buscar conocimiento</a></li>
  	<li><a href="/bitacora/base/base">Registrar en la base</a></li></ul></li>
  	<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Agenda<b class="caret"></b></a><ul class="dropdown-menu">
  	<li><a href="/bitacora/actividad/list">Actividades</a></li>
  	<li><a href="/bitacora/buscarActividad/busquedaActividad">Buscar Actividades</a></li></ul></li>
  	<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Biblioteca<b class="caret"></b></a><ul class="dropdown-menu">
  	<li><a href="/bitacora/documento/list">Biblioteca</a></li></ul></li></ul>
  	<ul class="nav navbar-nav navbar-right"><li><a href="/bitacora/alerta/list" ><i class="fa fa-exclamation-triangle"></i> Alertas (0)</a></li>
  	<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">admin (Administrador) <b class="caret"></b></a>
  	<ul class="dropdown-menu"><li><a href="/bitacora/persona/personal"><i class="fa fa-cogs"></i> Configuración</a></li><li class="divider"></li>
  	<li><a href="/bitacora/login/logout"><i class="fa fa-power-off"></i> Salir</a></li></ul></li></ul></div>
  	<!-- /.navbar-collapse --></div></nav>
  	"""

@register.simple_tag()
def menu_dos():
	menu = '''<ul class="nav nav-pills mb-5" style="background-color:#faeecf">'''
	mn_md = '''<li class="nav-item dropdown">
	    <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">{}</a>
	    	<div class="dropdown-menu">
	    '''
	mn_it = '''<a href="/{}" class="dropdown-item">{}</a>'''

	sql = "select mdlonmbr, mdlo__id from mdlo order by mdloordn"
	sql1 = "select accnnmbr, accn_url from accn where mdlo__id = {} order by accnordn"
	# print(sql)
	modulos = funciones.ejecutaSql(sql)
	# acciones = funciones.ejecutaSql(sql1)
	for d in modulos:
		# print("nombre: {}, id: {}".format(d[0], d[1]))
		menu += mn_md.format(d[0])
		for m in funciones.ejecutaSql(sql1.format(d[1])):
			menu += mn_it.format(m[1], m[0])
		menu += "</div></li>"
	menu += '''
	    <li class="nav-item dropdown ml-auto">
    		<a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">Usuario</a>
    		<div class="dropdown-menu dropdown-menu-right">
    			<a href="#" class="dropdown-item">Reports</a>
    			<a href="#" class="dropdown-item">Settings</a>
    		<div class="dropdown-divider"></div>
    			<a href="/salir"class="dropdown-item">Salir</a>
    		</div>
    	</li></ul>
	'''
	# print(menu)

	barra2 = '''
    	<li class="nav-item">
    		<a href="#" class="nav-link">Profile</a>
    	</li>
    	<li class="nav-item dropdown">
    		<a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">Messages</a>
    		<div class="dropdown-menu">
    			<a href="#" class="dropdown-item">Inbox</a>
    			<a href="#" class="dropdown-item">Drafts</a>
    			<a href="#" class="dropdown-item">Sent Items</a>
    		<div class="dropdown-divider"></div>
    			<a href="#"class="dropdown-item">Trash</a>
    		</div>
    	</li>
    	<li class="nav-item dropdown ml-auto">
    		<a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">Admin</a>
    		<div class="dropdown-menu dropdown-menu-right">
    			<a href="#" class="dropdown-item">Reports</a>
    			<a href="#" class="dropdown-item">Settings</a>
    		<div class="dropdown-divider"></div>
    			<a href="#"class="dropdown-item">Logout</a>
    		</div>
    	</li>
    </ul>
	'''
	texto = '''
	<ul class="nav nav-pills mb-5">
    	<li class="nav-item">
    		<a href="#" class="nav-link active">Home</a>
    	</li>
    	<li class="nav-item">
    		<a href="#" class="nav-link">Profile</a>
    	</li>
    	<li class="nav-item dropdown">
    		<a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">Messages</a>
    		<div class="dropdown-menu">
    			<a href="#" class="dropdown-item">Inbox</a>
    			<a href="#" class="dropdown-item">Drafts</a>
    			<a href="#" class="dropdown-item">Sent Items</a>
    		<div class="dropdown-divider"></div>
    			<a href="#"class="dropdown-item">Trash</a>
    		</div>
    	</li>
    	<li class="nav-item dropdown ml-auto">
    		<a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">Admin</a>
    		<div class="dropdown-menu dropdown-menu-right">
    			<a href="#" class="dropdown-item">Reports</a>
    			<a href="#" class="dropdown-item">Settings</a>
    		<div class="dropdown-divider"></div>
    			<a href="#"class="dropdown-item">Logout</a>
    		</div>
    	</li>
    </ul>
	'''

	# return texto
	return menu

# def menu(usro, apli):
#     items = []
#     if (usro):
#         strItems = ""
#         titulo = apli
#         if (usuario) {
#             def acciones = Prms.findAllByPerfil(perfil).accion.sort { it.modulo.orden }
#
#             acciones.each { ac ->
#                 if(ac.modulo.nombre != "noAsignado"){
#                     if (ac.tipo.id == 1) {
#                         if (!items[ac.modulo.nombre]) {
#                             items.put(ac.modulo.nombre, [ac.accnDescripcion, g.createLink(controller: ac.control.ctrlNombre, action: ac.accnNombre)])
#                         } else {
#                             items[ac.modulo.nombre].add(ac.accnDescripcion)
#                             items[ac.modulo.nombre].add(g.createLink(controller: ac.control.ctrlNombre, action: ac.accnNombre))
#                         }
#                     }
#                 }
#             }
#             items.each { item ->
#                 for (int i = 0; i < item.value.size(); i += 2) {
#                     for (int j = 2; j < item.value.size() - 1; j += 2) {
#                         def val = item.value[i].trim().compareTo(item.value[j].trim())
#                         if (val > 0 && i < j) {
#                             def tmp = [item.value[j], item.value[j + 1]]
#                             item.value[j] = item.value[i]
#                             item.value[j + 1] = item.value[i + 1]
#                             item.value[i] = tmp[0]
#                             item.value[i + 1] = tmp[1]
#                         }
#                     }
#                 }
#             }
#         } else {
#             items = ["Inicio": ["Prueba", "linkPrueba", "Test", "linkTest"]]
#         }
#
#         items.each { item ->
#             strItems += '<li class="dropdown">'
#             strItems += '<a href="#" class="dropdown-toggle" data-toggle="dropdown">' + item.key + '<b class="caret"></b></a>'
#             strItems += '<ul class="dropdown-menu">'
#
#             (item.value.size() / 2).toInteger().times {
#                 strItems += '<li><a href="' + item.value[it * 2 + 1] + '">' + item.value[it * 2] + '</a></li>'
#             }
#             strItems += '</ul>'
#             strItems += '</li>'
#         }
#
#         def alertas = "("
#         def count = Alerta.countByPersonaAndFechaRecibidoIsNull(usuario)
#         alertas += count
#         alertas += ")"
#
#         def html = "<nav class=\"navbar navbar-default navbar-fixed-top navbar-inverse\" role=\"navigation\">"
#
#         html += "<div class=\"container-fluid\">"
#
#         // Brand and toggle get grouped for better mobile display
#         html += '<div class="navbar-header">'
#         html += '<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">'
#         html += '<span class="sr-only">Toggle navigation</span>'
#         html += '<span class="icon-bar"></span>'
#         html += '<span class="icon-bar"></span>'
#         html += '<span class="icon-bar"></span>'
#         html += '</button>'
#         html += '<a class="navbar-brand navbar-logo" href="' + g.createLink(controller: 'inicio', action: 'index') +
#                 '"><img src="' + resource(dir: 'images', file: 'logo.png') + '" height="32px"/></a>'
#         html += '</div>'
#
#         // Collect the nav links, forms, and other content for toggling
#         html += '<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">'
#         html += '<ul class="nav navbar-nav">'
#         html += strItems
#         html += '</ul>'
#
#         html += '<ul class="nav navbar-nav navbar-right">'
# //        html += '<ul class="nav navbar-nav">'
#         html += '<li><a href="' + g.createLink(controller: 'alerta', action: 'list') + '" ' + ((count > 0) ? ' style="color:#ab623a" class="annoying"' : "") + '><i class="fa fa-exclamation-triangle"></i> Alertas ' + alertas + '</a></li>'
#         html += '<li class="dropdown">'
#         html += '<a href="#" class="dropdown-toggle" data-toggle="dropdown">' + usuario?.login + ' (' + session?.perfil + ')' + ' <b class="caret"></b></a>'
#         html += '<ul class="dropdown-menu">'
#         html += '<li><a href="' + g.createLink(controller: 'persona', action: 'personal') + '"><i class="fa fa-cogs"></i> Configuración</a></li>'
#         html += '<li class="divider"></li>'
#         html += '<li><a href="' + g.createLink(controller: 'login', action: 'logout') + '"><i class="fa fa-power-off"></i> Salir</a></li>'
#         html += '</ul>'
#         html += '</li>'
#         html += '</ul>'
#
#         html += '</div><!-- /.navbar-collapse -->'
#
#         html += "</div>"
#
#         html += "</nav>"
#
#         out << html
#     }