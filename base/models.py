from django.db import models
from django.contrib.auth.models import User

class Tema(models.Model):
    id = models.AutoField(db_column='tema__id', primary_key=True)
    descripcion = models.TextField(db_column='temadscr', max_length=63)
    class Meta:
        managed = True
        db_table = 'tema'

class Perfil(models.Model):
    id = models.AutoField(db_column='prfl__id', primary_key=True)
    descripcion = models.TextField(db_column='prfldscr', max_length=63)
    class Meta:
        managed = True
        db_table = 'prfl'

class Sesion(models.Model):
    id = models.AutoField(db_column='sesn__id', primary_key=True)
    inicio = models.DateTimeField(db_column='sesnfcin')
    fin = models.DateTimeField(db_column='sesnfcfn')
    usro = models.ForeignKey(
        User, db_column='usro__id', on_delete=models.CASCADE
    )
    class Meta:
        managed = True
        db_table = 'sesn'

class Base(models.Model):
    id = models.AutoField(db_column='base__id', primary_key=True)
    problema    = models.TextField(db_column='baseprbl', max_length=255)
    algoritmo   = models.TextField(db_column='basealgr', max_length=255)
    solucion    = models.TextField(db_column='baseslcn', blank=True)
    clave       = models.CharField(db_column='baseclve', max_length=127)
    referencia  = models.TextField(db_column='baserefe', max_length=255)
    observacion = models.TextField(db_column='baseobsr', max_length=255)
    fecha       = models.DateTimeField(db_column='basefcha', auto_now=True)

    tema = models.ForeignKey(
        Tema, db_column='tema__id', on_delete=models.CASCADE
    )

    class Meta:
        managed = True   # Django crea la tabla, False no se crea
        db_table = 'base'