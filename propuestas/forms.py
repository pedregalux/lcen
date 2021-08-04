from django import forms
from django.db import transaction
from django.forms import ModelForm
from propuestas.models import Propuesta



class CrearPropuestaForm(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'tema',
        'otros_temas',
        'problema',
        'situacion',
        'componente',
        'otras_organizaciones',
        'organizaciones_de_propuesta',
        'compromiso_convencionales',
        'convencionales_comprometidos',
        'anexo_propuesta',
        'titulo'
        ]
