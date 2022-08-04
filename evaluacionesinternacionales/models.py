from django.db import models


class EvaluadoraNormaInt(models.Model):
    nombre_eval_norma_int = models.CharField(
        "Nombre Evaluador@ Internacional",
        max_length=255,
        help_text="Nombre evaluador@ internacional")
    logo_org_eval_norma_int = models.ImageField(
        "Logo de la Evaluador@",
        upload_to='fotos_constituyentes/',
        null=True,
        blank=True,
        help_text="Logo")
    descripcion_eval_norma_int = models.TextField(
        "Descripción de la Evaluador@",
        null=True,
        blank=True,
        help_text="Descripción de la evaluador@")
    sitioweb_eval_norma_int = models.CharField(
        "Sitio Web de la Eval",
        null=True,
        max_length=255,
        blank=True,
        help_text="Profesión/País")
    class Meta:
        verbose_name = "Evaluador@"
        verbose_name_plural = "Evaluador@s"
    def __str__(self):
        return self.nombre_eval_norma_int

# Es la categoría general que agrupa normas, ej: Equidad de Género, etc
class CategoriaNormaInt(models.Model):
    tema_norma_int = models.CharField("Categoría de Norma Int",
        max_length=100,
        unique=True,
        help_text="Categoría de la norma")
    descripcion_cat_norma_int = models.TextField(
        "Descripción de la categoría de norma Int",
        null=True,
        blank=True,
        help_text="Descripción categoría de norma")
    icono_categoria_int = models.ImageField("Ícono Categoría Norma Int", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Categoría Normas Int"
        verbose_name_plural = "Categorías Normas Int"
    def __str__(self):
        return self.tema_norma_int


# La clase TagNorma es la que está asociada con el sello de cálidad
class TagNormaInt(models.Model):
    tag_norma_int = models.CharField("Tag de Norma Int",
        max_length=100,
        unique=True,
        help_text="Tag de la norma")
    descripcion_tag_norma_int = models.TextField(
        "Descripción de tag de norma Int",
        null=True,
        blank=True,
        help_text="Descripción tag de norma")
    icono_tag_int = models.ImageField("Ícono Sello Norma Int", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Tag Norma Int"
        verbose_name_plural = "Tag Normas Int"
    def __str__(self):
        return self.tag_norma_int


class NormaInt(models.Model):
    org_evaluadora_int = models.ForeignKey(EvaluadoraNormaInt,
        related_name="organizacion_eval_norma_int",
        verbose_name="Organización evaluadora",
        null=True,
        on_delete=models.SET_NULL)
    categoriadelanorma_int = models.ForeignKey(CategoriaNormaInt,
        related_name="categoria_eval_norma_int",
        verbose_name="Categoría de la norma",
        null=True,
        on_delete=models.SET_NULL)
    tags_norma_int = models.ManyToManyField(TagNormaInt,
        related_name="tags_de_norma_int",
        verbose_name="Tags/Sellos aplicados a la norma",
        blank=True)
    titulo_oficial_norma_int = models.TextField("Texto oficial de norma",
        null=True,
        blank=True,
        help_text="Texto oficial de la norma")
    titulo_web_norma_int = models.CharField("Título web de la norma",
        max_length=256,
        help_text="Título oficial de la norma")
    resumen_norma_int = models.TextField("Resumen de la norma",
        null=True,
        blank=True,
        help_text="Resumen de la norma")
    url_int = models.URLField(
        "URL de la Norma",
        null=True,
        blank=True,
        help_text="URL de la Norma")
    estandares_int = models.ImageField("Estándares Internacionales",
        upload_to='iconostemas/',
        null=True,
        blank=True,
        help_text="Según tu experiencia, ¿qué tan alineado está este artículo con los estándares internacionales o las prácticas de tu disciplina?")
    constituciones_int = models.ImageField("Constituciones Internacionales",
        upload_to='iconostemas/',
        null=True,
        blank=True,
        help_text="Según tu experiencia, ¿qué tan alineado está este artículo con los estándares establecidos por otras constituciones alrededor del mundo?")
    explicacion_int = models.TextField("Explicación Evaluación",
        null=True,
        blank=True,
        help_text="¿Podrías compartir algunas ideas en respaldo de tus respuestas anteriores?")
    mensaje_int = models.TextField("Mensaje",
        null=True,
        blank=True,
        help_text="¿Qué mensaje darías a las personas en Chile teniendo en cuenta que en septiembre votarán en el plebiscito en favor o rechazo de la nueva propuesta constitucional?")
    anexo_norma_pdf_int = models.FileField(upload_to='documents/',
        verbose_name="Documento del artículo",
        null=True,
        blank=True)
    anexo_norma_png_int = models.FileField(upload_to='documents/',
        verbose_name="Ilustración del artículo",
        null=True,
        blank=True)
    sello_norma_int = models.ImageField("Imagen/Sello de Norma", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Artículo Int"
        verbose_name_plural = "Artículos Int"
    def __str__(self):
        return self.titulo_web_norma_int
