from django.db import models
from usuarios.models import User, Ciudadano, Organizacion, Convencional
from mantenedores.models import Pais, Region, Comuna
from convencionales.models import Constituyente



class TemaPropuesta(models.Model):
    tema_propuesta = models.CharField("Tema de Propuesta",
        max_length=100,
        unique=True,
        help_text="Temas predefinidos de propuestas")
    icono_tema = models.ImageField("Ícono Temas Propuestas", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Tema Propuestas"
        verbose_name_plural = "Temas Propuestas"
    def __str__(self):
        return self.tema_propuesta



class SubtemaPropuesta(models.Model):
    subtema_propuesta = models.CharField("Subtema de Propuesta",
        max_length=100,
        unique=True,
        help_text="Subtemas predefinidos de propuestas")
    icono_tema = models.ImageField("Ícono Temas Propuestas", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Subtema Propuestas"
        verbose_name_plural = "Subtemas Propuestas"
    def __str__(self):
        return self.subtema_propuesta



class ComponenteConstitucion(models.Model):
    componente_constitucion = models.CharField("Componente Constitucional",
        max_length=100,
        unique=True,
        help_text="Componente Constitucional de Propuesta")
    class Meta:
        verbose_name = "Componente Constitucional"
        verbose_name_plural = "Componentes Constitucionales"
    def __str__(self):
        return self.componente_constitucion



class Propuesta(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # autor se asigna solo
    autor = models.ForeignKey(User,
        verbose_name="Autor@ de Propuesta",
        null=True,
        on_delete=models.SET_NULL)
    # paso 1
    pais = models.ForeignKey(Pais,
        related_name="pais_propuesta",
        verbose_name="País de Origen de Propuesta",
        null=True,
        on_delete=models.SET_NULL)
    region = models.ForeignKey(Region,
        related_name="region_propuesta",
        verbose_name="Región de Propuesta",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    comuna = models.ForeignKey(Comuna,
        related_name="comuna_propuesta",
        verbose_name="Comuna de Propuesta",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    # paso 2
    tema = models.ForeignKey(TemaPropuesta,
        null=True,
        on_delete=models.SET_NULL)
    otros_temas = models.ManyToManyField(SubtemaPropuesta,
        related_name="otros_temas_propuesta",
        verbose_name="Otros Temas de Propuesta")
    tema_extra = models.CharField("Tema complementario",
        max_length=100,
        null=True,
        blank=True)
    # paso 3
    problema = models.TextField("Descripción de problema a solucionar",
        null=True)
    situacion = models.TextField("Situación ideal de solución",
        null=True)
    componente = models.TextField("Componente de la Constitución",
        null=True)
    # paso 4
    otras_organizaciones = models.BooleanField("Junto a otras organizaciones",
        default=False)
    organizaciones_de_propuesta = models.TextField("Otras Organizaciones",
        null=True,
        blank=True)
    organizaciones = models.ManyToManyField(Organizacion,
        verbose_name="Otras Organizaciones de la Propuesta",
        blank=True,
        related_name="organizaciones_propuesta")
    #paso 5
    compromiso_convencionales = models.BooleanField("Convencionales comprometidos",
        default=False)
    # convencionales_comprometidos = models.ManyToManyField(Constituyente,
    #     related_name="convencionales_comprometidos",
    #     verbose_name="Nombres Convencionales Comprometidos",
    #     blank=True)
    # paso 6
    anexo_propuesta = models.FileField(upload_to='documents/',
        verbose_name="Anexos de la Propuesta",
        null=True,
        blank=True)
    anexo2_propuesta = models.FileField(upload_to='documents/',
        verbose_name="Otros anexos de la Propuesta-1",
        null=True,
        blank=True)
    anexo3_propuesta = models.FileField(upload_to='documents/',
        verbose_name="Otros anexos de la Propuesta-2",
        null=True,
        blank=True)
    link_extra1 = models.URLField(
        'Link a información complementaria -2-',
        null=True,
        blank=True,
        help_text="Ingresa la URL así: https://www.link.com")
    link_extra2 = models.URLField(
        'Link a información complementaria -1-',
        null=True,
        blank=True,
        help_text="Ingresa la URL así: https://www.link.com")
    # paso 7
    titulo = models.CharField("Título Propuesta",
        max_length=255,
        null=True)
    apoyos = models.ManyToManyField(User, related_name="apoyos_propuestas", through='ApoyoPropuesta')
    compromisos = models.ManyToManyField(User, related_name="compromisos_propuestas", through='CompromisoPropuesta')

    def __str__(self):
        return self.titulo

    @property
    def numapoyos_likes(self):
        return self.apoyos.all().count()

    @property
    def numcompromisos_likes(self):
        return self.compromisos.all().count()

    class Meta:
        verbose_name = "Propuesta Ciudadana"
        verbose_name_plural = "Propuestas Ciudadanas"





VALOR_CHOICES = (
    ('A', 'Apoyo'),
    ('N', 'No Apoyo'),
    )

class ApoyoPropuesta(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Usuario que apoya la propuesta",
        null=True,
        related_name="apoyo_propuesta",
        on_delete=models.SET_NULL)
    propuesta = models.ForeignKey(
        Propuesta,
        null=True,
        on_delete=models.SET_NULL)
    valor = models.CharField(choices=VALOR_CHOICES, default='Apoyo', max_length=10)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = "Apoyo Propuestas"
            verbose_name_plural = "Apoyos Propuestas"

    def __str__(self):
        return self.propuesta.titulo



COMP_CHOICES = (
    ('C', 'Compromiso'),
    ('N', 'No Compromiso'),
    )

class CompromisoPropuesta(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Usuario que se compromete con la propuesta",
        null=True,
        related_name="compromiso_propuesta",
        on_delete=models.SET_NULL)
    propuesta = models.ForeignKey(
        Propuesta,
        null=True,
        on_delete=models.SET_NULL)
    valor = models.CharField(choices=COMP_CHOICES, default='Compromiso', max_length=10)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = "Compromiso Propuestas"
            verbose_name_plural = "Compromisos Propuestas"

    def __str__(self):
        return self.propuesta.titulo
