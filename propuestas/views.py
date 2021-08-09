from django.shortcuts import render, redirect
from propuestas.models import Propuesta
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from formtools.wizard.views import SessionWizardView
from propuestas.forms import CrearPropuestaForm, PropuestaForm1, PropuestaForm2, PropuestaForm3, PropuestaForm4, PropuestaForm5, PropuestaForm6, PropuestaForm7


FORMS = [("crearpropuesta1", "propuestas.forms.PropuestaForm1"),
         ("crearpropuesta2", "propuestas.forms.PropuestaForm2"),
         ("crearpropuesta3", "propuestas.forms.PropuestaForm3"),
         ("crearpropuesta4", "propuestas.forms.PropuestaForm4"),
         ("crearpropuesta5", "propuestas.forms.PropuestaForm5"),
         ("crearpropuesta6", "propuestas.forms.PropuestaForm6"),
         ("crearpropuesta7", "propuestas.forms.PropuestaForm7")]

TEMPLATES = {"crearpropuesta1": "propuestas/crear_propuesta1.html",
             "crearpropuesta2": "propuestas/crear_propuesta2.html",
             "crearpropuesta3": "propuestas/crear_propuesta3.html",
             "crearpropuesta4": "propuestas/crear_propuesta4.html",
             "crearpropuesta5": "propuestas/crear_propuesta5.html",
             "crearpropuesta6": "propuestas/crear_propuesta6.html",
             "crearpropuesta7": "propuestas/crear_propuesta7.html"}



class VerPropuestasView(ListView):
    model = Propuesta
    context_object_name = 'propuestas_list'
    template_name = 'propuestas/ver_propuestas.html'



class VerPropuestaView(DetailView):
    model = Propuesta
    context_object_name = 'propuestas_detail'
    template_name = 'propuestas/ver_propuesta.html'



class PropuestaWizardView(SessionWizardView):
    # template_name = 'crear_propuesta.html'
    form_list = [PropuestaForm1, PropuestaForm2, PropuestaForm3, PropuestaForm4, PropuestaForm5, PropuestaForm6, PropuestaForm7]
    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })



class CrearPropuestaView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'propuestas.add_propuesta'
    form_class = CrearPropuestaForm
    template_name = 'propuestas/crear_propuesta.html'
    success_url = '/propuestas/'
    login_url = 'login'
    def form_valid(self, form):
        if form.is_valid():
            prop = form.save(commit=False)
            prop.autor = self.request.user
            form.save()
        return super().form_valid(form)
