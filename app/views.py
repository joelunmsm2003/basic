from django.shortcuts import render
from app.models import *
from django.contrib.auth.decorators import login_required


from django.views.decorators.csrf import csrf_exempt
import simplejson
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth import login

from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from app.serializers import *
from app.forms import *
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

# Create your views here.
def ingresar(request):

	if request.method == 'POST':

		user = request.POST['user']
		
		psw = request.POST['password']

		user = authenticate(username=user, password=psw)
	
		if user is not None:

			if user.is_active:

				login(request, user)

				try:

					_grupo = Group.objects.filter(user = request.user)[0]

					_agente = Agente.objects.get(user=request.user)
					_agente.estado_id=1
					_agente.save()

				except:

					return render(request, 'ingresar.html',{'error':'Asignar un grupo a tu usuario'})

				print 'grupo...',_grupo

				if str(_grupo) =='Admin':

					return HttpResponseRedirect("/admin")

				if str(_grupo)=='Agente':

					return HttpResponseRedirect("/agente/1")

	if request.method == 'GET':


		return render(request, 'ingresar.html',{})



def api_agentes(request):

	_data = Agente.objects.all()
	serializer =  AgentesSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

def lanzagestion(request,base,agente):


	redis_publisher = RedisPublisher(facility='foobar', users=['root'])

	message = RedisMessage('llamada')

	redis_publisher.publish_message(message)


	_data = Agente.objects.filter(id=agente)
	serializer =  AgentesSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

@login_required(login_url="/ingresar")
def m_agente(request,id_base):

	_agente=Agente.objects.get(user_id=request.user.id)

	for r in request.GET:

		if r=='estado':

			cambia_estado = request.GET['estado']

			_agente.estado_id=cambia_estado
			_agente.save()

			


	print _agente.estado_id

	_estado=Estado.objects.filter(id__in=[1,2])

	agenda = AgendarForm()

	agenteform = AgenteForm(instance=_agente)



	try:

		_base = Base.objects.get(id=id_base)

		form = BaseForm(instance=_base)

	except:

		return render(request, 'agente.html',{'error':'No existe en Base','agente':_agente,'estados':_estado})

	return render(request, 'agente.html',{'agenteform':agenteform,'agente':_agente,'agenda':agenda,'estados':_estado,'base':_base,'form':form})


@login_required(login_url="/ingresar")
def monitor(request):


	return render(request, 'monitor.html',{})