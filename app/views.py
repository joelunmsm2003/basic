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

				print 'llege aquis'

				try:

					_grupo = Group.objects.filter(user = request.user)[0]

					print _grupo

					if str(_grupo) =='Admin':

						return HttpResponseRedirect("/admin")


					if str(_grupo)=='Agente':

						_agente = Agente.objects.get(user=request.user)
						_agente.estado_id=1
						_agente.save()

						return HttpResponseRedirect("/agente/5268")



				except:

					

					return render(request, 'ingresar.html',{'error':'Consultar al admin'})

		return render(request, 'ingresar.html',{'error':'Usuario no existe'})




	if request.method == 'GET':


		return render(request, 'ingresar.html',{})



def api_agentes(request):

	_data = Agente.objects.all()
	serializer =  AgentesSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

def lanzagestion(request,base,agente):

	_agente = Agente.objects.get(id=agente)
	_agente.estado_id=3
	_agente.save()


	redis_publisher = RedisPublisher(facility='foobar', users=[_agente.user.username])

	message = RedisMessage('llamada-'+str(base))


	redis_publisher.publish_message(message)


	_data = Agente.objects.filter(id=agente)
	serializer =  AgentesSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)


def lanzafinllamada(request,base,agente):

	_agente = Agente.objects.get(id=agente)

	_agente.estado_id=4
	_agente.save()


	redis_publisher = RedisPublisher(facility='foobar', users=[_agente.user.username])

	message = RedisMessage('llamada-'+str(base))


	redis_publisher.publish_message(message)


	_data = Agente.objects.filter(id=agente)
	serializer =  AgentesSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)


def lanzaestado(request):

	# _agente = Agente.objects.get(id=agente)

	_agentes = Agente.objects.all()

	_agentes = AgentesSerializer(_agentes,many=True)

	redis_publisher = RedisPublisher(facility='foobar', users=['root'])

	message = RedisMessage(_agentes)

	redis_publisher.publish_message(message)

	data = simplejson.dumps('body')

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")

def m_agente(request,id_base):

	_agente=Agente.objects.get(user_id=request.user.id)


	# if request.method=='POST':

	# 	_agente.estado_id=2
	# 	_agente.save()


	# 	return HttpResponseRedirect("/agente/"+id_base)



	if request.method=='GET':


		print 'entre...',request.GET
	
		redis_publisher = RedisPublisher(facility='foobar', users=[_agente.user.username])

		message = RedisMessage('fin')

		redis_publisher.publish_message(message)

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