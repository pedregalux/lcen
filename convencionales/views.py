from django.shortcuts import render, redirect
from convencionales.models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView



class VerConvencionalesView(ListView):
    model = Constituyente
    context_object_name = 'constituyentes_list'
    template_name = 'convencionales/ver_convencionales.html'



class VerConvencionalView(DetailView):
    model = Constituyente
    context_object_name = 'constituyentes_detail'
    template_name = 'convencionales/ver_convencional.html'
