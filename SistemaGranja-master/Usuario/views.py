# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login

# Create your views here.
# def autenticar(request):
#     if request.method == 'POST':
#         action = request.POST.get('action', None)
#         usuario = request.POST.get('usuario', None)
#         clave = request.POST.get('clave', None)
#
#         if action == 'registrar':
#             user = User.objects.create_user(username=usuario,password=clave)
#             user.save()
#         elif action == 'login':
#             user = authenticate(username=usuario, password=clave)
#             login(request, user)
#         return redirect('/')
#
#     return render(request, 'login/login.html', {})

from django.shortcuts import render
from django.template import loader
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.template import loader
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreacionUsuarioForm
from django.contrib.auth.models import Group
from InicioSesion.mixins import JSONResponseMixin
from InicioSesion.mixins import LoginRequiredMixin


class UsuarioView(LoginRequiredMixin, TemplateView):
    template_name = 'auth/user_form.html'
    def get_context_data(self, **kwargs):
        context = super(UsuarioView, self).get_context_data(**kwargs)
        context.update({'form': CreacionUsuarioForm()})
        return context

class CrearUsuario(LoginRequiredMixin, CreateView):
    model = User
    success_url = reverse_lazy('usuarios:listar')
    fields = ['username','password','first_name','last_name','email','groups','is_active','is_superuser']

class ListarUsuarios(LoginRequiredMixin, ListView):
    model = User
    # template_name = 'user_list.html'
    # paginate_by = 5

class EditarUsuario(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CreacionUsuarioForm
    #success_url =

class BuscarUsuario(LoginRequiredMixin, JSONResponseMixin, DetailView):
    model = User
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return self.render_to_json_response()
    # def get_data(self):
    #     data = {
    #         'usuario':{
    #             'username': self.object.username,
    #             'first_name': self.object.first_name,
    #             'last_name': self.object.last_name,
    #             'is_superuser': self.object.is_superuser,
    #             'is_active': self.object.is_active
    #         }
    #     }
    #     return data
