import django_filters
from django_filters import filters
from django.forms import HiddenInput
from .models import Propuesta, TemaPropuesta, SubtemaPropuesta
from mantenedores.models import *


class PropuestaTemas(django_filters.FilterSet):
    tema = filters.ModelChoiceFilter(queryset=TemaPropuesta.objects.all().distinct(), label='', empty_label='Buscar por Tema...')
    comuna = filters.ModelChoiceFilter(queryset=Comuna.objects.all().distinct(), label='', empty_label='Buscar por Comuna...')
    otros_temas = filters.ModelChoiceFilter(queryset=SubtemaPropuesta.objects.all().distinct(), widget=HiddenInput())

    class Meta:
        model = Propuesta
        fields = ('otros_temas','tema','comuna',)
