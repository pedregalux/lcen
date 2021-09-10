import django_filters
from django_filters import filters
from .models import Propuesta, TemaPropuesta
from mantenedores.models import *


class PropuestaTemas(django_filters.FilterSet):
    tema = filters.ModelChoiceFilter(queryset=TemaPropuesta.objects.all().distinct(), label='', empty_label='Buscar por Tema...')
    comuna = filters.ModelChoiceFilter(queryset=Comuna.objects.all().distinct(), label='', empty_label='Buscar por Comuna...')

    class Meta:
        model = Propuesta
        fields = ('tema','comuna',)
