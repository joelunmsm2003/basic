from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import Group, User
import datetime

class Supervisor(models.Model):
    user = models.ForeignKey(User, db_column='user', blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today())

    def __unicode__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today())

    def __unicode__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today())
    


    def __unicode__(self):
        return self.nombre

class Campania(models.Model):

    fecha = models.DateTimeField(db_column='fecha cargada', default=datetime.datetime.today())  # Field renamed to remove unsuitable characters.
    archivo =  models.FileField(upload_to='static')
    cliente = models.ForeignKey(Cliente, db_column='cliente', blank=True, null=True)
    estado = models.ForeignKey(Estado, db_column='estado', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    # tipo = models.IntegerField(blank=True, null=True)
    # discado = models.IntegerField(blank=True, null=True)
    # factor = models.IntegerField(blank=True, null=True)
    # status = models.IntegerField(blank=True, null=True)
    # prefijo = models.IntegerField(blank=True, null=True)
    # troncal = models.IntegerField(blank=True, null=True)
    # timbrado1 = models.IntegerField(blank=True, null=True)
    # timbrado2 = models.IntegerField(blank=True, null=True)
    # grabacion = models.IntegerField(blank=True, null=True)
    # t1 = models.IntegerField(blank=True, null=True)
    # t2 = models.IntegerField(blank=True, null=True)
    # t3 = models.IntegerField(blank=True, null=True)
    # o_error_cnt = models.IntegerField(blank=True, null=True)
    # o_nocontesto_cnt = models.IntegerField(blank=True, null=True)
    # canales = models.IntegerField(blank=True, null=True)
    # timbrados = models.IntegerField(blank=True, null=True)
    # htinicio = models.TimeField(blank=True, null=True)
    # htfin = models.TimeField(blank=True, null=True)
    # mxllamada = models.IntegerField(blank=True, null=True)
    # llamadaxhora = models.IntegerField(blank=True, null=True)
    # hombreobjetivo = models.IntegerField(blank=True, null=True)
    # supervisor = models.ForeignKey(Supervisor, db_column='supervisor', blank=True, null=True)
    # tgestion = models.IntegerField(blank=True, null=True)
    # password = models.CharField(max_length=100, blank=True)
    # inactividad = models.IntegerField(blank=True, null=True)
    # acd = models.IntegerField(db_column='ACD',blank=True, null=True)   # Field name made lowercase

    def __unicode__(self):
        return self.nombre


# Create your models here.
class Base(models.Model):

    codigo  =models.CharField(max_length=100,blank=True,null=True)
    nombres =models.CharField(max_length=100,blank=True,null=True)
    apellidos  =models.CharField(max_length=100,blank=True,null=True)
    dni =models.CharField('DNI',max_length=100,blank=True,null=True)
    telefono_1=models.CharField(max_length=100,blank=True,null=True)
    telefono_2 =models.CharField(max_length=100,blank=True,null=True)
    importe=models.CharField(max_length=100,blank=True,null=True)
    deuda_pendiente=models.CharField(max_length=100,blank=True,null=True)
    campania = models.ForeignKey(Campania, db_column='campania', blank=True, null=True)
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today()) 


# Create your models here.
class Api(models.Model):

    host  =models.CharField(max_length=100,blank=True,null=True)
    url  =models.CharField(max_length=100,blank=True,null=True)
    metodo  =models.CharField(max_length=100,blank=True,null=True)
    header  =models.CharField(max_length=100,blank=True,null=True)
    body =models.CharField(max_length=100,blank=True,null=True)
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today())


class Agente(models.Model):

    anexo = models.IntegerField(blank=True, null=True)
    fono = models.IntegerField(blank=True, null=True)
    #tiempo = models.DateTimeField(blank=True, null=True)
    destino = models.IntegerField(blank=True, null=True)
    duracion = models.TimeField(blank=True, null=True)
    atendidas = models.IntegerField(blank=True, null=True)
    contactadas = models.IntegerField(blank=True, null=True)
    estado = models.ForeignKey('Estado', db_column='estado', blank=True, null=True)
    est_ag_predictivo = models.IntegerField(blank=True, null=True)
    canal = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, db_column='user', blank=True, null=True)
    supervisor = models.ForeignKey(Supervisor, db_column='supervisor', blank=True, null=True)
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today())
    # disponible = models.IntegerField(blank=True, null=True)
    # tiniciogestion = models.DateTimeField(blank=True, null=True)
    # tfingestion = models.DateTimeField(blank=True, null=True)
    # tiniciollamada = models.DateTimeField(blank=True, null=True)
    # tfinllamada = models.DateTimeField(blank=True, null=True)
    # tinicioespera = models.DateTimeField(blank=True, null=True)
    # tfinespera = models.DateTimeField(blank=True, null=True)
    # tiniciotipeo = models.DateTimeField(blank=True, null=True)
    # wordstipeo = models.IntegerField(blank=True, null=True)
    # tiniciopausa = models.DateTimeField(blank=True, null=True)
    # checa = models.CharField(max_length=100, blank=True)
    # checabreak = models.CharField(max_length=100, blank=True)
    # tiniciobreak = models.DateTimeField(blank=True, null=True)
    # checaser = models.CharField(max_length=100, blank=True)
    # tinicioservicio = models.DateTimeField(blank=True, null=True)


    class Meta:
        verbose_name = 'Agente'







    