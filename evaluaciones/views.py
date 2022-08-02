from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Norma,CategoriaNorma,TagNorma,OrganizacionNorma
from .filters import NormaCategorias
from django.db.models import Q



class VerHomeEvaluacionesView(ListView):
    model = Norma
    context_object_name = 'evaluaciones_list'
    template_name = 'evaluaciones/homeevaluaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['simbolos'] = TagNorma.objects.all()
        return context


class VerEvaluacionesView(ListView):
    model = Norma
    context_object_name = 'evaluaciones_list'
    template_name = 'evaluaciones/verevaluaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['simbolos'] = TagNorma.objects.all()
        context['filtrocategorias'] = NormaCategorias(self.request.GET, queryset=self.get_queryset())
        return context


class VerEvaluacionView(DetailView):
    model = Norma
    context_object_name = 'evaluacion_detail'
    template_name = 'evaluaciones/verevaluacion.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['relacionadas'] = Norma.objects.filter(categoriadelanorma=self.object)
    #     return context


class VerHomeEvaluacionView(DetailView):
    model = Norma
    context_object_name = 'evaluacion_detail'
    template_name = 'evaluaciones/homeevaluacion.html'


class VerOrgsEvalView(ListView):
    model = OrganizacionNorma
    context_object_name = 'orgs_evaluaciones_list'
    template_name = 'evaluaciones/verorgsevaluadoras.html'


class VerOrgEvalView(DetailView):
    model = OrganizacionNorma
    context_object_name = 'organizaciones_detail'
    template_name = 'evaluaciones/verorgevaluadora.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['evaluaciones'] = Norma.objects.filter(org_evaluadora=self.object)
        return context

class SearchResultsView(ListView):
    model = Norma
    template_name = 'evaluaciones/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Norma.objects.filter(Q(titulo_oficial_norma__icontains=query) | Q(titulo_web_norma__icontains=query))
        return object_list

class SearchResultView(DetailView):
    model = Norma
    context_object_name = 'evaluacion_detail'
    template_name = 'evaluaciones/verevaluacion.html'