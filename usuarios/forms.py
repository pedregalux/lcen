from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django import forms
from django.forms import ModelForm
from django.db import transaction
from mantenedores.models import Pais, Region, Comuna, Distrito, Alcance
from .models import User, Ciudadano, Organizacion, Convencional
from django.contrib.auth.models import Group



class CiudadanoSignUpForm(UserCreationForm):
    username = forms.CharField(label='Nombre Usuario')
    password1 = forms.CharField(label='Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    nombre = forms.CharField(label='Nombre y Apellido', required=True)
    email = forms.EmailField(required=True)
    genero = forms.CharField(label='Seleccionar Género', required=False, widget=forms.Select(choices=Ciudadano.GENERO))
    rangoedad = forms.CharField(label='Seleccionar rango de edad', required=False, widget=forms.Select(choices=Ciudadano.RANGOEDAD))
    pais = forms.ModelChoiceField(queryset=Pais.objects, empty_label="Seleccionar País")
    region = forms.ModelChoiceField(queryset=Region.objects, empty_label="Seleccionar Región")
    comuna = forms.ModelChoiceField(queryset=Comuna.objects, empty_label="Seleccionar Comuna")
    # cualquiercosa = forms.CharField(required=False)

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
        # ciudadano.cualquiercosa=self.cleaned_data.get('cualquiercosa')
        ciudadano.save()
        return user



class OrganizacionSignUpForm(UserCreationForm):

    # datos de registro
    username = forms.CharField(
        label='Nombre Usuario',
        required = True,
        help_text="Este nombre, junto a una contraseña, es necesario para ingresar a la plataforma")
    password1 = forms.CharField(
        label='Contraseña',
        required = True,
        widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        required = True,
        widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    nombre = forms.CharField(
        label='Nombre de la Organización',
        help_text="Nombre oficial de la Organización, no se puede modificar",
        required=True)
    email = forms.EmailField(
        label='E-mail de registro',
        required=True,
        help_text="Este e-mail se usará para acciones como recuperación de contraseña y no se mostrará al público")

    # datos públicos del pefil
    nombre_perfil = forms.CharField(
        label='Nombre para Perfil de la Organización',
        help_text="Este es el nombre que será mostrado en el Perfil Público de la Organización en la plataforma",
        required=True)
    logo_organizacion = forms.ImageField(
        label='Logo/Imagen de la Organización',
        help_text="Si deseas subir una imagen o logo representativo de tu organización al perfil público, lo puedes cargar acá",
        required=True)
    descripcion = forms.CharField(
        widget=forms.Textarea,
        label='Reseña de la Organización',
        required=False,
        help_text="Este es la reseña oficial de la Organización y se usará en el perfil público")

    # datos de ubicación
    pais = forms.ModelChoiceField(
        queryset=Pais.objects,
        required=False,
        empty_label="Seleccionar País")
    region = forms.ModelChoiceField(
        queryset=Region.objects,
        required=False,
        empty_label="Seleccionar Región")
    comuna = forms.ModelChoiceField(
        queryset=Comuna.objects,
        required=False,
        empty_label="Seleccionar Comuna")
    alcance = forms.ModelChoiceField(
        queryset=Alcance.objects,
        required=False,
        help_text="Selecciona el alcance territorial del trabajo de tu organiación.",
        empty_label="Seleccionar Alcance")

    # redes sociales
    sitioweb = forms.URLField(
        label='Sitio Web de la Organización',
        help_text="Ingresa la dirección de tu sitio así: https://www.organizacion.com. Quedará publicado en el perfil público.",
        required=False)
    twitter = forms.URLField(
        label='Twitter de la Organización',
        help_text="Ingresa la dirección de tu perfil así: https://www.twitter.com/miorganizacion. Quedará publicado en el perfil público.",
        required=False)
    facebook = forms.URLField(
        label='Facebook de la Organización',
        help_text="Ingresa la dirección de tu perfil así: https://www.facebook.com/miorganizacion. Quedará publicado en el perfil público.",
        required=False)
    instagram = forms.URLField(
        label='Instagram de la Organización',
        help_text="Ingresa la dirección de tu perfil así: https://www.instagram.com/miorganizacion. Quedará publicado en el perfil público.",
        required=False)
    linkedin = forms.URLField(
        label='LinkedIn de la Organización',
        help_text="Ingresa la dirección de tu perfil así: https://www.instagram.com/miorganizacion. Quedará publicado en el perfil público.",
        required=False)

    # de contacto privado
    nombre_contacto = forms.CharField(
        label='Nombre Contacto',
        required=False,
        help_text="Este nombre de contacto no será difundido públicamente")
    email_contacto = forms.EmailField(
        help_text="No será difundido públicamente",
        required=False)
    telefono_contacto = forms.CharField(
        help_text="No será difundido públicamente",
        required=False)

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

        organizacion.pais=self.cleaned_data.get('pais')
        organizacion.region=self.cleaned_data.get('region')
        organizacion.comuna=self.cleaned_data.get('comuna')
        organizacion.alcance=self.cleaned_data.get('alcance')

        organizacion.nombre_perfil=self.cleaned_data.get('nombre_perfil')
        organizacion.descripcion=self.cleaned_data.get('descripcion')

        organizacion.sitioweb=self.cleaned_data.get('sitioweb')
        organizacion.twitter=self.cleaned_data.get('twitter')
        organizacion.facebook=self.cleaned_data.get('facebook')
        organizacion.instagram=self.cleaned_data.get('instagram')
        organizacion.linkedin=self.cleaned_data.get('linkedin')

        organizacion.nombre_contacto=self.cleaned_data.get('nombre_contacto')
        organizacion.email_contacto=self.cleaned_data.get('email_contacto')
        organizacion.telefono_contacto=self.cleaned_data.get('telefono_contacto')

        organizacion.logo_organizacion=self.cleaned_data.get('logo_organizacion')

        organizacion.save()
        return user



class OrganizacionChangeForm(ModelForm):

    class Meta:
        model = Organizacion
        fields = ('nombre_perfil','descripcion','pais','region','comuna','alcance','sitioweb','twitter','facebook','instagram','linkedin','nombre_contacto','email_contacto','telefono_contacto','logo_organizacion')



class ConvencionalSignUpForm(UserCreationForm):
    username = forms.CharField(label='Nombre Usuario', help_text="El Nombre de Usuario es para identificarse en la plataforma, debe ser en minúsculas, sin espacios y sólo letras y/o números.")
    password1 = forms.CharField(label='Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    nombre = forms.CharField(label='Nombre y Apellido', required=True)
    email = forms.EmailField(required=True)
    # cualquiercosa = forms.CharField(required=False)

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
        # convencional.cualquiercosa=self.cleaned_data.get('cualquiercosa')
        convencional.save()
        return user



class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'your class',
        'placeholder': 'Ingrese acá el e-mail',
        'type': 'email',
        'name': 'email'
        }))
