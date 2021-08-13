from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .forms import CiudadanoSignUpForm, OrganizacionSignUpForm, ConvencionalSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User



def register(request):
    return render(request, '../templates/register.html')



class ciudadano_register(CreateView):
    model = User
    form_class = CiudadanoSignUpForm
    template_name = '../templates/ciudadano_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/inicio')



class organizacion_register(CreateView):
    model = User
    form_class = OrganizacionSignUpForm
    template_name = '../templates/organizacion_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/inicio')



class convencional_register(CreateView):
    model = User
    form_class = ConvencionalSignUpForm
    template_name = '../templates/convencional_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/inicio')



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
            username=username,
            password=password)
            if user is not None :
                login(request,user)
                return redirect('/propuestas/crearpropuestas')
            else:
                messages.error(request,"La contraseña o usuari@ no corresponden. Por favor revisa bien.")
        else:
                messages.error(request,"La contraseña o usuari@ no corresponden. Por favor revisa bien.")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})



def logout_view(request):
    logout(request)
    return redirect('/inicio')
