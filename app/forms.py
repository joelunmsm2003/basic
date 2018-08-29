from django import forms
from django.forms import ModelForm,Textarea
from app.models import *

class BaseForm(ModelForm):
    class Meta:
        model = Base
        fields = ('nombres', 'apellidos','dni','telefono_1','telefono_2','importe','deuda_pendiente')
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control '}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control '}),
            'dni': forms.TextInput(attrs={'class': 'form-control '}),
            'telefono_1': forms.TextInput(attrs={'class': 'form-control '}),
            'telefono_2': forms.TextInput(attrs={'class': 'form-control '}),
            'importe': forms.TextInput(attrs={'class': 'form-control '}),
            'deuda_pendiente': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AgendarForm(forms.Form):
	fecha = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control col-md-3','type':'date'}))
	descripcion = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control','rows':"3"}))


class AgenteForm(ModelForm):
    class Meta:
        model = Agente
        fields = ('estado',)
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-control '}),
        }