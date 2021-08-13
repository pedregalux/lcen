import os
from django.conf import settings
from django.shortcuts import render, redirect
from propuestas.models import Propuesta
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView, TemplateView
from django.core.files.storage import FileSystemStorage
from formtools.wizard.views import SessionWizardView
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin



FORMS2 = [("p1", PropuestaForm1),
          ("p2", PropuestaForm2),
          ("p3", PropuestaForm3),
          ("p4", PropuestaForm4),
          ("p5", PropuestaForm5),
          ("p6", PropuestaForm6),
          ("p7", PropuestaForm7)]

TEMPLATES2 = {"p1": "propuestas/crear_propuesta1.html",
              "p2": "propuestas/crear_propuesta2.html",
              "p3": "propuestas/crear_propuesta3.html",
              "p4": "propuestas/crear_propuesta4.html",
              "p5": "propuestas/crear_propuesta5.html",
              "p6": "propuestas/crear_propuesta6.html",
              "p7": "propuestas/crear_propuesta7.html"}



class VerPropuestasView(ListView):
    model = Propuesta
    context_object_name = 'propuestas_list'
    template_name = 'propuestas/ver_propuestas.html'



class VerPropuestaView(DetailView):
    model = Propuesta
    context_object_name = 'propuestas_detail'
    template_name = 'propuestas/ver_propuesta.html'



class PropuestaWizardView(LoginRequiredMixin,SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES2[self.steps.current]]
    instance = None
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'documents'))

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Propuesta()
        return self.instance

    def done(self, form_list, **kwargs):
        self.instance.autor = self.request.user
        self.instance.save()
        return render(self.request, 'done.html')




# class CrearPropuestaView(FormView):
#     permission_required = 'propuestas.add_propuesta'
#     form_class = CrearPropuestaForm
#     template_name = 'propuestas/crear_propuesta.html'
#     success_url = '/propuestas/'
#     login_url = 'login'
#     def form_valid(self, form):
#         if form.is_valid():
#             prop = form.save(commit=False)
#             prop.autor = self.request.user
#             form.save()
#         return super().form_valid(form)
