from django.shortcuts import render
from django.http import HttpResponse
from propuestas.models import Propuesta
from usuarios.models import Organizacion
from django.views.generic import TemplateView
from django.db.models import Count



class LandingView(TemplateView):
    template_name = 'inicio/presentacion.html'



class EsperaView(TemplateView):
    template_name = 'inicio/en_construccion.html'



class HomeView(TemplateView):
    template_name = 'inicio/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['organizaciones'] = Organizacion.objects.all()
        context['propuestas'] = Propuesta.objects.annotate(apoyos_count=Count('apoyos')).order_by('-autor__organizacion','-apoyos_count')[:3]
        return context



class QueesView(TemplateView):
    template_name = 'inicio/que_es.html'



class PreguntasView(TemplateView):
    template_name = 'inicio/preguntas-frecuentes.html'



class EnsayosView(TemplateView):
    template_name = 'inicio/ensayos.html'



class EnsayotomounoView(TemplateView):
    template_name = "inicio/ensayo-tomouno.html"



class EnsayotomodosView(TemplateView):
    template_name = "inicio/ensayo-tomodos.html"



class EnsayotomotresView(TemplateView):
    template_name = "inicio/ensayo-tomotres.html"



class EnsayotomocuatroView(TemplateView):
    template_name = "inicio/ensayo-tomocuatro.html"



class EnsayotomocincoView(TemplateView):
    template_name = "inicio/ensayo-tomocinco.html"



class TerminosView(TemplateView):
    template_name = 'inicio/terminos.html'



def error404(request, exception, template_name='inicio/error.html'):
    return render(request, template_name)

def error500(request, template_name='inicio/error.html'):
    return render(request, template_name)

def error403(request, exception, template_name='inicio/error.html'):
    return render(request, template_name)

def error400(request, exception, template_name='inicio/error.html'):
    return render(request, template_name)
