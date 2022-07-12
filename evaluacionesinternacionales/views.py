from django.shortcuts import render
rom django.views.generic import ListView
from django.views.generic import DetailView
from .models import NormaInt,EvaluadoraNormaInt,TagNormaInt,CategoriaNormaInt


class VerEvaluacionesIntView(ListView):
    model = NormaInt
    context_object_name = 'evaluaciones_int_list'
    template_name = 'evaluacionesinternacionales/verevaluacionesint.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['simbolos'] = TagNorma.objects.all()
    #     context['filtrocategorias'] = NormaCategorias(self.request.GET, queryset=self.get_queryset())
    #     return context


class VerEvaluacionIntView(DetailView):
    model = NormaInt
    context_object_name = 'evaluacion_int_detail'
    template_name = 'evaluacionesinternacionales/verevaluacionint.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['relacionadas'] = Norma.objects.filter(categoriadelanorma=self.object)
    #     return context
