from django.contrib.auth.models import User
from app.models import *
from rest_framework import serializers


class AgentesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Agente
		#fields = ('id', 'nombre','tipo_agente')
		fields = '__all__'





# class HistorialGloboSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = HistorialGlobo
# 		#fields = ('id', 'nombre','tipo_agente')
# 		fields = '__all__'
