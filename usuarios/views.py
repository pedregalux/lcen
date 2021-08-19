from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import CiudadanoSignUpForm, OrganizacionSignUpForm, ConvencionalSignUpForm, OrganizacionChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Organizacion
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin



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



class organizacion_update(UpdateView):
    form_class = OrganizacionChangeForm
    template_name = 'usuarios/updateorg.html'

    def dispatch(self, request, *args, **kwargs):
        if not (self.request.user.is_authenticated and self.request.user.is_organizacion):
            return HttpResponseNotFound()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user.organizacion

    def form_valid(self, form):
        organizacion = form.save()
        return redirect('/inicio')



class VerOrganizacionesView(ListView):
    model = Organizacion
    context_object_name = 'organizaciones_list'
    template_name = 'usuarios/verorgs.html'



class VerOrganizacionView(DetailView):
    model = Organizacion
    context_object_name = 'organizaciones_detail'
    template_name = 'usuarios/verorg.html'



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
                next = request.GET.get('next', '/inicio' )
                return redirect(next)
            else:
                messages.error(request,"La contraseña o usuari@ no corresponden. Por favor revisa bien.")
        else:
                messages.error(request,"La contraseña o usuari@ no corresponden. Por favor revisa bien.")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})



def logout_view(request):
    logout(request)
    return redirect('/inicio')
