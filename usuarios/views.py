from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import CiudadanoSignUpForm, OrganizacionSignUpForm, ConvencionalSignUpForm, OrganizacionChangeForm
from django.contrib.auth.forms import AuthenticationForm
from propuestas.models import Propuesta
from .models import User, Organizacion, Convencional
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
    context_object_name = 'organizacion'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_creadas'] = Propuesta.objects.filter(autor=self.object.user)
        context['lista_apoyadas'] = Propuesta.objects.filter(apoyos=self.object.user)
        return context



class VerConvencionalesView(ListView):
    model = Convencional
    context_object_name = 'constituyentes_list'
    template_name = 'usuarios/verconstituyentes.html'



class VerConvencionalView(DetailView):
    model = Convencional
    context_object_name = 'constituyentes_detail'
    template_name = 'usuarios/verconstituyente.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_comprometidas'] = Propuesta.objects.filter(compromisos=self.object.user)
        return context



class VerPropuestasConvencionalView(ListView):
    model = Propuesta
    context_object_name = 'propuestas_list'
    template_name = 'usuarios/ver_propuestas_convencional.html'

    def get_queryset(self):
        return Propuesta.objects.annotate(compromisos_count=Count('compromisos')).order_by('-compromisos_count')

    def dispatch(self, request, *args, **kwargs):
        if not (self.request.user.is_authenticated and self.request.user.is_convencional):
            return redirect('loginconvencionales')
        return super().dispatch(request, *args, **kwargs)



class VerPropuestaConvencionalView(DetailView):
    model = Propuesta
    context_object_name = 'propuestas_detail'
    template_name = 'usuarios/ver_propuesta_convencional.html'

    def dispatch(self, request, *args, **kwargs):
        if not (self.request.user.is_authenticated and self.request.user.is_convencional):
            return redirect('loginconvencionales')
        return super().dispatch(request, *args, **kwargs)



def CompromisoView(request, pk):
    apyo = Propuesta.objects.get(pk=pk)
    apyo.compromisos.add(request.user)
    return HttpResponseRedirect(reverse('verpropuestaconvencionales', args=[str(pk)]))



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



def login_convencionales(request):
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
                next = request.GET.get('next', 'verpropuestasconvencionales' )
                return redirect(next)
            else:
                messages.error(request,"La contraseña o usuari@ no corresponden. Por favor revisa bien.")
        else:
                messages.error(request,"La contraseña o usuari@ no corresponden. Por favor revisa bien.")
    return render(request, '../templates/login_convencionales.html',
    context={'form':AuthenticationForm()})




def logout_view(request):
    logout(request)
    return redirect('/inicio')
