from django.db import models
from usuarios.models import User
from mantenedores.models import Pais, Region, Comuna
from convencionales.models import Constituyente



class TemaPropuesta(models.Model):
    tema_propuesta = models.CharField("Tema de Propuesta",
        max_length=100,
        unique=True,
        help_text="Temas predefinidos de propuestas")
    class Meta:
        verbose_name = "Tema Propuestas"
        verbose_name_plural = "Temas Propuestas"
    def __str__(self):
        return self.tema_propuesta



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
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Selecciona tu país")
    region = models.ForeignKey(Region,
        related_name="region_propuesta",
        verbose_name="Región de Propuesta",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Si la propuesta es regional, señala la región.")
    comuna = models.ForeignKey(Comuna,
        related_name="comuna_propuesta",
        verbose_name="Comuna de Propuesta",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Si la propuesta es comunal, señala la comuna.")
    # paso 2
    tema = models.ForeignKey(TemaPropuesta,
        null=True,
        on_delete=models.SET_NULL,
        help_text="¿Cuál es el tema principal de tu propuesta? Por favor selecciona una categoría del siguiente listado, pues nos ayudará a organizar temáticamente las propuestas en el buscador de la plataforma.")
    otros_temas = models.ManyToManyField(TemaPropuesta,
        related_name="otros_temas_propuesta",
        verbose_name="Otros Temas de Propuesta",
        blank=True,
        help_text="¿Qué otros temas aborda tu propuesta? Por favor selecciona hasta tres temas adicionales.")
    # paso 3
    problema = models.TextField("Descripción de problema a solucionar",
        max_length=225,
        null=True,
        blank=True,
        help_text="¿Cuál es el problema que tú o tu organización busca solucionar?")
    situacion = models.TextField("Situación ideal de solución",
        null=True,
        blank=True,
        help_text="Con respecto al problema planteado, ¿cuál sería la situación ideal?")
    componente = models.TextField("Componente de la Constitución",
        null=True,
        blank=True,
        help_text="Para avanzar en el logro de esa situación ideal, ¿qué debería contemplar la Nueva Constitución?")
    # paso 4
    otras_organizaciones = models.BooleanField("Junto a otras organizaciones",
        default=False,
        help_text="¿Esta propuesta fue elaborada en conjunto con otras organizaciones?")
    organizaciones_de_propuesta = models.TextField("Otras Organizaciones",
        null=True,
        blank=True,
        help_text="Si tu respuesta fue 'sí', por favor escribe cuáles (separadas por comas). No te olvides de incluir a tu organización.")
    #paso 5
    compromiso_convencionales = models.BooleanField("Convencionales comprometidos",
        default=False,
        help_text="¿Tu propuesta cuenta con compromisos formales de apoyo de convencionales constituyentes?")
    convencionales_comprometidos = models.ManyToManyField(Constituyente,
        related_name="convencionales_comprometidos",
        verbose_name="Nombres Convencionales Comprometidos",
        blank=True,
        help_text="Si tu respuesta fue 'sí', por favor marca todos los/as convencionales que se comprometieron con tu propuesta. Por favor considera que verificaremos esta información.")
    # paso 6
    anexo_propuesta = models.FileField(upload_to='documents/',
        verbose_name="Anexos de la Propuesta",
        null=True,
        blank=True,
        help_text="Si has elaborado un documento de tu propuesta en extenso, por favor adjúntalo. Asimismo, si cuentas con otros materiales (estudios, encuestas, presentaciones, material comunicacional, etc.) que complementen tu propuesta, agrégalos.")
    # paso 7
    titulo = models.CharField("Título Propuesta",
        max_length=255,
        null=True,
        help_text="Por favor, revisa el resumen de tu propuesta y escribe un título atractivo para que podamos difundirla hacia la ciudadanía y la Convención Constitucional.")
    class Meta:
        verbose_name = "Propuesta Ciudadana"
        verbose_name_plural = "Propuestas Ciudadanas"
    def __str__(self):
        return self.titulo
