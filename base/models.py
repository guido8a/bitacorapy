from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Tema(models.Model):
    id = models.AutoField(db_column='tema__id', primary_key=True)
    descripcion = models.TextField(db_column='temadscr', max_length=63)

    def __str__(self):

        return self.descripcion

    class Meta:
        # managed = True
        managed = False
        db_table = 'tema'

class Perfil(models.Model):
    id = models.AutoField(db_column='prfl__id', primary_key=True)
    descripcion = models.TextField(db_column='prfldscr', max_length=63)
    class Meta:
        # managed = True
        managed = False
        db_table = 'prfl'

class Sesion(models.Model):
    id = models.AutoField(db_column='sesn__id', primary_key=True)
    inicio = models.DateTimeField(db_column='sesnfcin')
    fin = models.DateTimeField(db_column='sesnfcfn')
    usro = models.ForeignKey(
        User, db_column='usro__id', on_delete=models.CASCADE
    )
    class Meta:
        # managed = True
        managed = False
        db_table = 'sesn'

class Base(models.Model):
    id = models.AutoField(db_column='base__id', primary_key=True)
    problema    = models.TextField(db_column='baseprbl', max_length=255)
    algoritmo   = models.TextField(db_column='basealgr', max_length=255)
    solucion    = models.TextField(db_column='baseslcn', blank=True)
    clave       = models.CharField(db_column='baseclve', max_length=127, blank=True)
    referencia  = models.TextField(db_column='baserefe', max_length=255, blank=True)
    observacion = models.TextField(db_column='baseobsr', max_length=255, blank=True)
    fecha       = models.DateTimeField(db_column='basefcha', auto_now=True)

    tema = models.ForeignKey(
        Tema, db_column='tema__id', on_delete=models.CASCADE
    )

    class Meta:
        # managed = True   # Django crea la tabla, False no se crea
        managed = False
        db_table = 'base'

class Modulo(models.Model):
    id = models.AutoField(db_column='mdlo__id', primary_key=True)
    nombre = models.TextField(db_column='mdlonmbr', max_length=255)
    orden  = models.IntegerField(db_column='mdloordn')

    class Meta:
        managed = True   # Django crea la tabla, False no se crea
        # managed = False
        db_table = 'mdlo'

class Accion(models.Model):
    id = models.AutoField(db_column='accn__id', primary_key=True)
    nombre = models.TextField(db_column='accnnmbr', max_length=63)
    url = models.TextField(db_column='accn_url', max_length=31)
    orden  = models.IntegerField(db_column='accnordn')

    modulo = models.ForeignKey(
        Modulo, db_column='mdlo__id', on_delete=models.CASCADE
    )

    class Meta:
        managed = True   # Django crea la tabla, False no se crea
        # managed = False
        db_table = 'accn'