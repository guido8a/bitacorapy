from django.contrib import admin
from . import models

class TemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ('descripcion',)

admin.site.register(models.Tema, TemaAdmin)

class BaseAdmin(admin.ModelAdmin):
    list_display = ('tema', 'problema', 'algoritmo', 'fecha')
    list_filter = ('tema', 'problema', 'algoritmo', 'fecha')
    search_fields = ('tema', 'problema', 'algoritmo', 'fecha')

admin.site.register(models.Base, BaseAdmin)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)

admin.site.register(models.Perfil, PerfilAdmin)
