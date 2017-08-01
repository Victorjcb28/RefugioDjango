 # -*- coding: utf-8 -*-
from __future__ import absolute_import #importarlo para las llaves foraneas
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django .views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import MascotaForm
from .models import Mascota


# Create your views here.

def index(request):
	return render(request,'mascota/index.html')

def mascota_view(request):
	
	form= MascotaForm(request.POST or None)
	if form.is_valid():
		#instance=form.cleaned_data
		#instance=form.save(commit=False)
		#instance.save()
		form.save()
	#return redirect('mascota:index')

	
	context={

		"form":form,	

	}


	return render(request,'mascota/mascota_form.html',context)

def mascota_list(request):
	mascota= Mascota.objects.all().order_by('id')
	contexto={'mascotas':mascota}
	return render (request, 'mascota/mascota_list.html',contexto)

def mascota_edit(request, id_mascota):
	mascota=Mascota.objects.get(id=id_mascota)	

	if request.method=='GET':
		form=MascotaForm(instance=mascota)
	else:
		form=MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_delete(request, id_mascota):
	mascota=Mascota.objects.get(id=id_mascota)
	if request.method=='POST':
		mascota.delete()
		return redirect ('mascota:mascota_listar')
	return render(request,'mascota/mascota_delete.html',{'mascota':mascota})


class MascotaList(ListView):
	model= Mascota
	template_name= 'mascota/mascota_list.html'

class MascotaCreate(CreateView):

	model=Mascota
	form_class=MascotaForm
	template_name= 'mascota/mascota_form.html'
	success_url= reverse_lazy('mascota:mascota_listar')

class MascotaUpdate(UpdateView):
	model= Mascota
	form_class=MascotaForm
	template_name= 'mascota/mascota_form.html'
	success_url= reverse_lazy('mascota:mascota_listar')

class MascotaDelete(DeleteView):
	model= Mascota
	template_name='mascota/mascota_delete.html'
	success_url=reverse_lazy('mascota:mascota_listar')




