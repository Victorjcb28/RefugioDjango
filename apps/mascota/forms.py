from __future__ import absolute_import #importarlo para las llaves foraneas
from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		fields = [
			"nombre",
			"sexo",
			"edad_aproximada",
			"fecha_rescate",
			"persona",
			"vacuna",
		]
		
		labels={
			'nombre':'nombre',
			'sexo': 'sexo',
			'edad_aproximada':'edad',
			'fecha_rescate':'fecha',
			'persona':'persona',
			'vacuna':'vacuna',

		}

		widgets={
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'sexo':forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate':forms.TextInput(attrs={'class':'form-control'}),
			'persona':forms.Select(attrs={'class':'form-control'}),
			'vacuna':forms.CheckboxSelectMultiple(),


		}
