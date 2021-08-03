from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from managers.models import Pais, Region, Comuna, Distrito
from .models import User, Ciudadano, Organizacion, Convencional
from django.contrib.auth.models import Group



class CiudadanoSignUpForm(UserCreationForm):
    username = forms.CharField(label='Nombre Usuario')
    password1 = forms.CharField(label='Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    nombre = forms.CharField(label='Nombre y Apellido', required=True)
    email = forms.EmailField(required=True)
    genero = forms.CharField(required=False, widget=forms.Select(choices=Ciudadano.GENERO))
    rangoedad = forms.CharField(required=False, widget=forms.Select(choices=Ciudadano.RANGOEDAD))
    pais = forms.ModelChoiceField(queryset=Pais.objects, empty_label="Seleccionar País")
    region = forms.ModelChoiceField(queryset=Region.objects, empty_label="Seleccionar Región")
    comuna = forms.ModelChoiceField(queryset=Comuna.objects, empty_label="Seleccionar Comuna")
    cualquiercosa = forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_ciudadano = True
        user.nombre = self.cleaned_data.get('nombre')
        user.save()
        ciudadano = Ciudadano.objects.create(user=user)
        ciudadano.email=self.cleaned_data.get('email')
        ciudadano.genero=self.cleaned_data.get('genero')
        ciudadano.rangoedad=self.cleaned_data.get('rangoedad')
        ciudadano.pais=self.cleaned_data.get('pais')
        ciudadano.region=self.cleaned_data.get('region')
        ciudadano.comuna=self.cleaned_data.get('comuna')
        ciudadano.cualquiercosa=self.cleaned_data.get('cualquiercosa')
        ciudadano.save()
        return user



class OrganizacionSignUpForm(UserCreationForm):
    username = forms.CharField(label='Nombre Usuario')
    password1 = forms.CharField(label='Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    nombre = forms.CharField(label='Nombre Organización/Colectivo', required=True)
    email = forms.EmailField(required=True)
    email_contacto = forms.EmailField(required=True)
    telefono_contacto = forms.CharField(required=False)
    cualquiercosa = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_organizacion = True
        user.nombre = self.cleaned_data.get('nombre')
        user.save()
        organizacion = Organizacion.objects.create(user=user)
        organizacion.email=self.cleaned_data.get('email')
        organizacion.email_contacto=self.cleaned_data.get('email_contacto')
        organizacion.telefono_contacto=self.cleaned_data.get('telefono_contacto')
        organizacion.cualquiercosa=self.cleaned_data.get('cualquiercosa')
        organizacion.save()
        return user



class ConvencionalSignUpForm(UserCreationForm):
    username = forms.CharField(label='Nombre Usuario')
    password1 = forms.CharField(label='Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    nombre = forms.CharField(label='Nombre y Apellido', required=True)
    email = forms.EmailField(required=True)
    cualquiercosa = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_convencional = True
        user.nombre = self.cleaned_data.get('nombre')
        user.save()
        convencional = Convencional.objects.create(user=user)
        convencional.email=self.cleaned_data.get('email')
        convencional.cualquiercosa=self.cleaned_data.get('cualquiercosa')
        convencional.save()
        return user
