from django.db import models

class OrganizacionNorma(models.Model):
    nombre_org_norma = models.CharField(
        "Nombre Organización",
        max_length=255,
        help_text="Nombre web de la organización")
    logo_org_norma = models.ImageField(
        "Logo de la Organización",
        upload_to='fotos_constituyentes/',
        null=True,
        blank=True,
        help_text="Logo")
    descripcion_org_norma = models.TextField(
        "Descripción de la Organización",
        null=True,
        blank=True,
        help_text="Descripción organización")

# Es la categoría general que agrupa normas, ej: Equidad de Género, etc
class CategoriaNorma(models.Model):
    tema_norma = models.CharField("Categoría de Norma",
        max_length=100,
        unique=True,
        help_text="Categoría de la norma")
    descripcion_cat_norma = models.TextField(
        "Descripción de la categoría de norma",
        null=True,
        blank=True,
        help_text="Descripción categoría de norma")
    icono_categoria = models.ImageField("Ícono Categoría Norma", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Categoría Normas"
        verbose_name_plural = "Categorías Normas"
    def __str__(self):
        return self.tema_norma


# La clase TagNorma es la que está asociada con el sello de cálidad
class TagNorma(models.Model):
    tag_norma = models.CharField("Tag de Norma",
        max_length=100,
        unique=True,
        help_text="Tag de la norma")
    descripcion_tag_norma = models.TextField(
        "Descripción de tag de norma",
        null=True,
        blank=True,
        help_text="Descripción tag de norma")
    icono_tag = models.ImageField("Ícono Tag Norma", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Tag Norma"
        verbose_name_plural = "Tag Normas"
    def __str__(self):
        return self.tag_norma

# La norma
class Norma(models.Model):
    org_evaluadora = models.ForeignKey(OrganizacionNorma,
        related_name="organizacion_eval_norma",
        verbose_name="Organización evaluadora",
        null=True,
        on_delete=models.SET_NULL)
    categoriadelanorma = models.ForeignKey(CategoriaNorma,
        related_name="organizacion_eval_norma",
        verbose_name="Organización evaluadora",
        null=True,
        on_delete=models.SET_NULL)
    titulo_oficial_norma = models.TextField("Título oficial de norma",
        unique=True,
        help_text="Título oficial de la norma")
    titulo_web_norma = models.CharField("Título web de la norma",
        max_length=256,
        unique=True,
        help_text="Título oficial de la norma")
    resumen_norma = models.TextField("Resumen de la norma",
        help_text="Resumen de la norma")
    importancia_para_chile = models.IntegerField("Importancia para Chile",
        null=True,
        blank=True,
        help_text="¿Cuán importante es este artículo(s) para la calidad de vida de las personas en Chile?")
    razones_importancia_norma = models.TextField("Razones de importancia de norma",
        null=True,
        blank=True,
        help_text="¿Por qué este artículo(s) tiene la importancia para la calidad de vida que indicaste en la pregunta anterior?")
    mejora_de_cp80 = models.IntegerField("Mejora de constitución anterior",
        null=True,
        blank=True,
        help_text="En el marco de una agenda de justicia social, económica y de derechos humanos: ¿en qué medida la Nueva Constitución mejora respecto de la Constitución actualmente vigente?")
    sello_norma = models.ImageField("Sello de Norma", upload_to='iconostemas/', null=True, blank=True)
