#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from app.models import *
from django.contrib.admin import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import os.path
import json
import requests
from django.contrib.admin.filters import DateFieldListFilter
import pandas as pd

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')


@admin.register(Campania)
class CampaniaAdmin(admin.ModelAdmin):
	list_display = ('id','fecha')

	def save_model(self, request, obj, form, change):
		
		super(CampaniaAdmin, self).save_model(request, obj, form, change)

		caption = str(Campania.objects.get(id=obj.id).archivo)

		df = pd.read_excel(caption)

		for i in range(df.shape[0]):

			print i

			codigo = df['Codigo'][i]
			nombres = df['Nombres'][i]
			apellidos = df['Apellido Paterno'][i]
			dni = df['Num Docum Ident'][i]
			telefono_1 = df['Telf 1'][i]
			telefono_2 = df['Telf 2'][i]
			deuda_pendiente = df['Importe Deuda Pendiente'][i]



			Base(campania_id=obj.id,codigo=codigo,nombres=nombres,apellidos=apellidos,dni=dni,telefono_1=telefono_1,telefono_2=telefono_2,deuda_pendiente=deuda_pendiente).save()


		

	
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	
@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
	list_display = ('id','nombres','apellidos','dni','telefono_1','telefono_2','importe','deuda_pendiente')
	list_filter=('campania',)

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
	list_display = ('id','anexo')
	list_filter=('supervisor',)

@admin.register(Api)
class ApiAdmin(admin.ModelAdmin):
	list_display = ('id','host','url','metodo','header')



	