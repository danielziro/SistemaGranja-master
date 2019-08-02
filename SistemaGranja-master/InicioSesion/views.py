from .forms import InicioSesionForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import FormView

# Create your views here.
class InicioSesionView(FormView):
    form_class = InicioSesionForm
    template_name = 'InicioSesion/login.html'
    success_url = '/principal/'
    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(InicioSesionView, self).form_valid(form)

def principal(request):
    return render(request,'principal/principal.html',{})

#def autenticar(request):
    #return render(request, 'hello.html', {})
    # if request.method == 'POST':
    #     action = request.POST.get('action', None)
    #     usuario = request.POST.get('usuario', None)
    #     clave = request.POST.get('clave', None)
    #
    #     if action == 'registrar':
    #         user = User.objects.create_user(username=usuario,password=clave)
    #         user.save()
    #     elif action == 'login':
    #         user = authenticate(username=usuario, password=clave)
    #         login(request, user)
    #     return redirect('/')
    # context = {}
    # return render(request, 'hello.html', {})
