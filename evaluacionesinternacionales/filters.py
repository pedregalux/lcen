import django_filters
from django_filters import filters
from django.forms import HiddenInput
from .models import NormaInt,CategoriaNormaInt,TagNormaInt,EvaluadoraNormaInt



class NormaCategoriasInt(django_filters.FilterSet):
    categoriaint = filters.ModelChoiceFilter(queryset=CategoriaNormaInt.objects.all().distinct(), widget=HiddenInput())

    class Meta:
        model = NormaInt
        fields = ('categoriadelanorma_int',)
