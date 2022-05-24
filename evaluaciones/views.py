from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Norma


class VerEvaluacionesView(ListView):
    model = Norma
    context_object_name = 'evaluaciones_list'
    template_name = 'evaluaciones/verevaluaciones.html'


class VerEvaluacionView(DetailView):
    model = Norma
    context_object_name = 'evaluacion_detail'
    template_name = 'evaluaciones/verevaluacion.html'
