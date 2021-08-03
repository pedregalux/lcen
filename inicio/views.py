from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView



class LandingView(TemplateView):
    template_name = 'inicio/presentacion.html'

class EsperaView(TemplateView):
    template_name = 'inicio/en_construccion.html'

class HomeView(TemplateView):
    template_name = 'inicio/home.html'

class QueesView(TemplateView):
    template_name = 'inicio/que_es.html'
