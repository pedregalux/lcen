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
        labels = {
            'pais': ('1. País'),
            'region': ('2. Región'),
            'comuna': ('3. Comuna'),
        }
        help_texts = {
            'pais': ('Selecciona tu país'),
            'region': ('Selecciona tu región'),
            'comuna': ('Selecciona tu comuna'),
        }



class PropuestaForm2(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'tema',
        'otros_temas'
        ]
        labels = {
            'tema': ('1. ¿Cuál es el tema principal de tu propuesta?'),
            'otros_temas': ('2. ¿Qué otros temas aborda tu propuesta?'),
        }
        help_text = {
            'tema': ('Selecciona tema principal'),
            'otros_temas': ('Por favor selecciona hasta tres temas adicionales'),
        }



class PropuestaForm3(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'problema',
        'situacion',
        'componente'
        ]
        labels = {
            'problema': ('1. País'),
            'situacion': ('2. Región'),
            'componente': ('2. Región'),
        }
        help_text = {
            'problema': ('1. País'),
            'situacion': ('2. Región'),
            'componente': ('2. Región'),
        }



class PropuestaForm4(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'otras_organizaciones',
        'organizaciones_de_propuesta'
        ]
        labels = {
            'otras_organizaciones': ('1. País'),
            'organizaciones_de_propuesta': ('2. Región'),
        }
        help_text = {
            'otras_organizaciones': ('1. País'),
            'organizaciones_de_propuesta': ('2. Región'),
        }



class PropuestaForm5(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'compromiso_convencionales',
        'convencionales_comprometidos'
        ]
        labels = {
            'compromiso_convencionales': ('1. País'),
            'convencionales_comprometidos': ('2. Región'),
        }
        help_text = {
            'compromiso_convencionales': ('1. País'),
            'convencionales_comprometidos': ('2. Región'),
        }



class PropuestaForm6(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'anexo_propuesta'
        ]
        labels = {
            'anexo_propuesta': ('1. País'),
        }



class PropuestaForm7(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'titulo'
        ]
        labels = {
            'titulo': ('1. País'),
        }



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
