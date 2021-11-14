import django_filters
from django_filters import filters
from django.forms.widgets import TextInput
from .models import User, Convencional
from mantenedores.models import *
from convencionales.models import *


class ConvencionalesFiltro(django_filters.FilterSet):

    lista = filters.ModelChoiceFilter(queryset=Lista.objects.all().distinct(), label='', empty_label='Buscar Colectivo')
    distrito = filters.ModelChoiceFilter(queryset=Distrito.objects.all().distinct(), label='', empty_label='Buscar Distrito')
    cargo = filters.ModelChoiceFilter(queryset=Cargo.objects.all().distinct(), label='', empty_label='Buscar Comisión')
    email = django_filters.CharFilter(lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Buscar por Apellido'}), label='Buscar Apellido')
    # movimiento = filters.ModelChoiceFilter(queryset=Movimiento.objects.all().distinct(), label='', empty_label='Buscar por Partido/Movimiento...')



    class Meta:
        model = Convencional
        fields = ('lista','cargo','distrito','email',)
