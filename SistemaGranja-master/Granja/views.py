from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader

#Decorators
from django.contrib.auth.decorators import login_required

# Class-Based views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from django.core.urlresolvers import reverse_lazy
from .forms import GranjaForm
from .models import Granja

from Usuario.mixins import LoginRequiredMixin

# Create your views here.

#Implementacion de un formulario
# @login_required()
# def new_granja(request):
#     if request.method == 'POST':
#         form = GranjaForm(request.POST, request.FILES)
#         if form.is_valid():
#             granja = form.save()
#             granja.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = GranjaForm()
#
#     template = loader.get_template('new_granja.html')
#     context = {
#         'form' : form
#     }
#     return HttpResponse(template.render(context, request))

class CrearGranja(LoginRequiredMixin, CreateView):
    model = Granja
    success_url = reverse_lazy('granja:listar')
    form_class = GranjaForm

class ListarGranja(ListView):
    model = Granja

class ConsultarGranja(LoginRequiredMixin, DetailView):
    model = Granja

class EliminarGranja(LoginRequiredMixin, DeleteView):
    model = Granja
    success_url = reverse_lazy('granja:listar')
