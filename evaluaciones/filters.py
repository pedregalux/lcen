import django_filters
from django_filters import filters
from django.forms import HiddenInput
from .models import Norma,CategoriaNorma,TagNorma,OrganizacionNorma



class NormaCategorias(django_filters.FilterSet):
    categoria = filters.ModelChoiceFilter(queryset=CategoriaNorma.objects.all().distinct(), widget=HiddenInput())

    class Meta:
        model = Norma
        fields = ('categoriadelanorma',)
