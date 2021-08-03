from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import Group
from mantenedores.models import Pais, Region, Distrito, Comuna



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
    email_contacto = models.EmailField(max_length=255)
    telefono_contacto = models.CharField(max_length=255)
    cualquiercosa = models.CharField(max_length=255)
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
