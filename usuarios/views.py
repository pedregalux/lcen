from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .filters import ConvencionalesFiltro
from .forms import CiudadanoSignUpForm, OrganizacionSignUpForm, ConvencionalSignUpForm, OrganizacionChangeForm, UserPasswordResetForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from propuestas.models import Propuesta, TemaPropuesta
from propuestas.filters import PropuestaTemas
from .models import User, Organizacion, Convencional
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes




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
        context['lista_cocreadas'] = Propuesta.objects.filter(organizaciones=self.object.id)
        context['lista_apoyadas'] = Propuesta.objects.filter(apoyos=self.object.user)
        return context



class VerConvencionalesView(ListView):
    paginate_by = 12
    model = Convencional
    context_object_name = 'constituyentes_list'
    template_name = 'usuarios/verconstituyentes.html'

    def get_queryset(self):
        return Convencional.objects.order_by('email')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtroconvencionales'] = ConvencionalesFiltro(self.request.GET, queryset=self.get_queryset())
        return context



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
        return Propuesta.objects.annotate(apoyos_count=Count('apoyos')).order_by('-autor__organizacion','-apoyos_count')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtropropuestas'] = PropuestaTemas(self.request.GET, queryset=self.get_queryset())
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comprometidos'] = Propuesta.objects.filter(compromisos=self.object.compromisos.all())
        return context



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



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = UserPasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Cambio de Contraseña en LCeN - La Constitución es Nuestra"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'laconstitucionesnuestra.cl',
					'site_name': 'LCeN',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'https',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'soporte@laconstitucionesnuestra.cl' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = UserPasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})
