import django_filters
from django_filters import filters
from .models import Propuesta, TemaPropuesta
from mantenedores.models import *


class PropuestaTemas(django_filters.FilterSet):
    tema = filters.ModelChoiceFilter(queryset=TemaPropuesta.objects.all(), label='', empty_label='Ordenar por Tema...')
    class Meta:
        model = Propuesta
        fields = ('tema',)
