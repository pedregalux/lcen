from django.db import models
from evaluaciones.models import OrganizacionNorma,CategoriaNorma,TagNorma

# Create your models here.

class Norma(models.Model):
    org_evaluadora_int = models.ForeignKey(OrganizacionNorma,
        related_name="organizacion_eval_norma_int",
        verbose_name="Organización evaluadora",
        null=True,
        on_delete=models.SET_NULL)
    categoriadelanorma_int = models.ForeignKey(CategoriaNorma,
        related_name="categoria_eval_norma_int",
        verbose_name="Categoría de la norma",
        null=True,
        on_delete=models.SET_NULL)
    tags_norma_int = models.ManyToManyField(TagNorma,
        related_name="tags_de_norma_int",
        verbose_name="Tags/Sellos aplicados a la norma",
        blank=True)
    titulo_oficial_norma_int = models.TextField("Texto oficial de norma",
        help_text="Texto oficial de la norma")
    titulo_web_norma_int = models.CharField("Título web de la norma",
        max_length=256,
        help_text="Título oficial de la norma")
    resumen_norma_int = models.TextField("Resumen de la norma",
        help_text="Resumen de la norma")
    url_int = models.URLField(
        "URL de la Norma",
        null=True,
        blank=True,
        help_text="URL de la Norma")
    importancia_para_chile_int = models.ImageField("Importancia para Chile",
        upload_to='iconostemas/',
        null=True,
        blank=True,
        help_text="¿Cuán importante es este artículo(s) para la calidad de vida de las personas en Chile?")
    razones_importancia_norma_int = models.TextField("Razones de importancia de norma",
        null=True,
        blank=True,
        help_text="¿Por qué este artículo(s) tiene la importancia para la calidad de vida que indicaste en la pregunta anterior?")
    mejora_de_cp80_int = models.ImageField("Mejora de constitución anterior",
        upload_to='iconostemas/',
        null=True,
        blank=True,
        help_text="En el marco de una agenda de justicia social, económica y de derechos humanos: ¿en qué medida la Nueva Constitución mejora respecto de la Constitución actualmente vigente?")
    razones_mejora_cp80_int = models.TextField("Razones de mejora de constitución anterior",
        null=True,
        blank=True,
        help_text="¿Cómo puedes justificar la opción asignada en la pregunta anterior?")
    presencia_otros_paises_int = models.TextField("Presencia en otros países",
        null=True,
        blank=True,
        help_text="¿Hay presencia de artículos similares en otros países? Explícanos en qué países y en qué se parecen")
    historia_norma_int = models.TextField("Historia de la norma",
        null=True,
        blank=True,
        help_text="¿Cuál es la historia de este artículo en términos de su creación social?")
    mitos_norma_int = models.TextField("Mitos de la norma",
        null=True,
        blank=True,
        help_text="¿Cuáles son los principales mitos asociados al artículo(s) y porqué son mitos?")
    futurista_norma_int = models.TextField("Futuro de la norma",
        null=True,
        blank=True,
        help_text="Imagina que estamos en 2052: ¿Cómo es tu entorno y la vida de las personas en Chile después de este artículo(s)?")
    aporte_desarrollo_int = models.TextField("Aporte al desarrollo",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta al desarrollo del país?")
    aporte_ddhh_natura_int = models.TextField("Aporte DDHH y naturaleza",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta al respeto a los derechos humanos y de la naturaleza?")
    aporte_seguridad_int = models.TextField("Aporte seguridad y certeza",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a la seguridad y certeza de las personas en Chile?")
    aporte_igualdad_int = models.TextField("Aporte a la igualdad",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a la igualdad entre todas las personas?")
    aporte_innovacion_int = models.TextField("Aporte a la innovación y sustentabilidad",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a la innovación y sustentabilidad?")
    aporte_descentralizacion_int = models.TextField("Aporte a la descentralización",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a los procesos de descentralización?")
    aporte_contra_corrupcion_int = models.TextField("Aporte contra la corrupción",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a los procesos de participación y a la lucha contra la corrupción?")
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
