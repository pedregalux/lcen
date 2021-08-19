from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import Group
from mantenedores.models import Pais, Region, Distrito, Comuna, Alcance



class User(AbstractUser):
    is_ciudadano = models.BooleanField(default=False)
    is_organizacion = models.BooleanField(default=False)
    is_convencional = models.BooleanField(default=False)
    nombre = models.CharField("Nombre",
        max_length=255)
    last_login = models.DateTimeField(blank=True,
        null=True,
        verbose_name='last login')



class Ciudadano(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    GENERO = (
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('No Binario', 'No Binario'),
        ('No Declara', 'No Declara'),
        )
    genero = models.CharField("Género",
        max_length=100,
        choices=GENERO)
    RANGOEDAD = (
        ('-20', '-20'),
        ('20-29', '20-29'),
        ('30-39', '30-39'),
        ('40-49', '40-49'),
        ('50-59', '50-59'),
        ('60-69', '60-69'),
        ('70+', '70+'),
        ('No Declara', 'No Declara'),
        )
    rangoedad = models.CharField("Rango Edad",
        max_length=100,
        choices=RANGOEDAD)
    pais = models.ForeignKey(Pais,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    region = models.ForeignKey(Region,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    comuna = models.ForeignKey(Comuna,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    cualquiercosa = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Ciudadan@"
        verbose_name_plural = "Ciudadan@s"
    def __str__(self):
        return self.user.username



class Organizacion(models.Model):

    user = models.OneToOneField(User,
        on_delete = models.CASCADE)
    email = models.EmailField(max_length=255)

    # datos públicos del pefil
    nombre_perfil = models.CharField(
        'Nombre Perfil',
        max_length=255,
        help_text="Este es el nombre que será mostrado en el Perfil Público de la Organización en la plataforma")
    logo_organizacion = models.ImageField(
        'Logo/Imagen de la Organización',
        null=True,
        blank=True,
        help_text="Si deseas subir una imagen o logo representativo de tu organización al perfil público, lo puedes cargar acá")
    descripcion = models.TextField(
        'Reseña de la Organización',
        null=True,
        blank=True,
        help_text="Este es la reseña oficial de la Organización y se usará en el perfil público")

    # datos de ubicación
    pais = models.ForeignKey(Pais, null=True, on_delete=models.SET_NULL)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    comuna = models.ForeignKey(Comuna, null=True, on_delete=models.SET_NULL)
    alcance = models.ForeignKey(Alcance, null=True, on_delete=models.SET_NULL)

    # redes sociales
    sitioweb = models.URLField(
        'Sitio Web de la Organización',
        null=True,
        blank=True,
        help_text="Ingresa la dirección de tu sitio así: https://www.organizacion.com. Quedará publicado en el perfil público.")
    twitter = models.URLField(
        'Twitter de la Organización',
        null=True,
        blank=True,
        help_text="Ingresa la dirección de tu perfil así: https://www.twitter.com/miorganizacion. Quedará publicado en el perfil público.")
    facebook = models.URLField(
        'Facebook de la Organización',
        null=True,
        blank=True,
        help_text="Ingresa la dirección de tu perfil así: https://www.facebook.com/miorganizacion. Quedará publicado en el perfil público.")
    instagram = models.URLField(
        'Instagram de la Organización',
        null=True,
        blank=True,
        help_text="Ingresa la dirección de tu perfil así: https://www.instagram.com/miorganizacion. Quedará publicado en el perfil público.")
    linkedin = models.URLField(
        'LinkedIn de la Organización',
        null=True,
        blank=True,
        help_text="Ingresa la dirección de tu perfil así: https://www.instagram.com/miorganizacion. Quedará publicado en el perfil público.")

    # de contacto privado
    nombre_contacto = models.CharField(
        'Nombre Contacto',
        max_length=255,
        null=True,
        blank=True,
        help_text="Este nombre de contacto no será difundido públicamente")
    email_contacto = models.EmailField(
        help_text="No será difundido públicamente",
        null=True,
        blank=True)
    telefono_contacto = models.CharField(
        max_length=255,
        help_text="No será difundido públicamente",
        null=True,
        blank=True)

    class Meta:
        verbose_name = "Organzación"
        verbose_name_plural = "Organizaciones"
    def __str__(self):
        return self.user.username



class Convencional(models.Model):
    user = models.OneToOneField(User,
        on_delete = models.CASCADE)
    email = models.EmailField(max_length=255)
    cualquiercosa = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Convencional"
        verbose_name_plural = "Convencionales"
    def __str__(self):
        return self.user.username
