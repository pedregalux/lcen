from django import forms
from django.db import transaction
from django.forms import ModelForm
from propuestas.models import Propuesta, TemaPropuesta
from mantenedores.models import *



class PropuestaForm1(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'pais',
        'region',
        'comuna'
        ]


class PropuestaForm2(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'tema',
        'otros_temas'
        ]


class PropuestaForm3(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'problema',
        'situacion',
        'componente'
        ]


class PropuestaForm4(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'otras_organizaciones',
        'organizaciones_de_propuesta'
        ]


class PropuestaForm5(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'compromiso_convencionales',
        'convencionales_comprometidos'
        ]


class PropuestaForm6(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'anexo_propuesta'
        ]


class PropuestaForm7(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'titulo'
        ]


# class CrearPropuestaForm(forms.ModelForm):
#     class Meta:
#         model = Propuesta
#         fields = [
#         'pais',
#         'region',
#         'comuna',
#         'tema',
#         'otros_temas',
#         'problema',
#         'situacion',
#         'componente',
#         'otras_organizaciones',
#         'organizaciones_de_propuesta',
#         'compromiso_convencionales',
#         'convencionales_comprometidos',
#         'anexo_propuesta',
#         'titulo'
#         ]
