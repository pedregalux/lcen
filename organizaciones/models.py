from django.db import models
from mantenedores.models import Pais, Region, Comuna, Alcance



class OrganizacionProfile(models.Model):
    nombre = models.CharField("Nombre Organización",
        max_length=255,
        unique=True)
    sigla = models.CharField("Sigla Organización",
        max_length=50,
        unique=True)
    logo = models.ImageField("Logo Organización",
        upload_to='logos/',
        null=True,
        blank=True)
    descripcion = models.TextField("Descripción",
        null=True,
        blank=True)
    email = models.EmailField("E-mail de Contacto",
        max_length=254,
        null=True,
        blank=True)
    twitter = models.URLField("Twitter",
        max_length=254,
        null=True,
        blank=True)
    facebook = models.URLField("Facebook",
        max_length=254,
        null=True,
        blank=True)
    instagram = models.URLField("Instagram",
        max_length=254,
        null=True,
        blank=True)
    sitioweb = models.URLField("Sitio web",
        max_length=254,
        null=True,
        blank=True)
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
    alcance = models.ManyToManyField(Alcance,
        blank=True)
    class Meta:
        verbose_name = "Organización Profile"
        verbose_name_plural = "Organizaciones Profiles"
    def __str__(self):
        return self.nombre
