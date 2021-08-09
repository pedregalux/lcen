from django import forms
from django.db import transaction
from django.forms import ModelForm
from propuestas.models import Propuesta
from mantenedores.models import Pais, Region, Comuna



class PropuestaForm1(forms.Form):
    pais = forms.ModelChoiceField(queryset=Pais.objects.all())
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())



class PropuestaForm2(forms.Form):
    subject = forms.CharField(max_length=100)



class PropuestaForm3(forms.Form):
    subject = forms.CharField(max_length=100)



class PropuestaForm4(forms.Form):
    subject = forms.CharField(max_length=100)



class PropuestaForm5(forms.Form):
    subject = forms.CharField(max_length=100)



class PropuestaForm6(forms.Form):
    subject = forms.CharField(max_length=100)



class PropuestaForm7(forms.Form):
    subject = forms.CharField(max_length=100)



# class PropuestaForm8(forms.Form):
#     subject = forms.CharField(max_length=100)

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
