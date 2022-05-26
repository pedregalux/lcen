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
    sitioweb = models.URLField(
        "Sitio Web de la Organización",
        null=True,
        blank=True,
        help_text="URL de la organización")
    class Meta:
        verbose_name = "Organización"
        verbose_name_plural = "Organizaciones"
    def __str__(self):
        return self.nombre_org_norma

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
    icono_tag = models.ImageField("Ícono Sello Norma", upload_to='iconostemas/', null=True, blank=True)
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
        related_name="categoria_eval_norma",
        verbose_name="Categoría de la norma",
        null=True,
        on_delete=models.SET_NULL)
    tags_norma = models.ManyToManyField(TagNorma,
        related_name="tags_de_norma",
        verbose_name="Tags/Sellos aplicados a la norma",
        blank=True)
    titulo_oficial_norma = models.CharField("Título oficial de norma",
        max_length=256,
        help_text="Título oficial de la norma")
    titulo_web_norma = models.CharField("Título web de la norma",
        max_length=256,
        help_text="Título oficial de la norma")
    resumen_norma = models.TextField("Resumen de la norma",
        help_text="Resumen de la norma")
    url = models.URLField(
        "URL de la Norma",
        null=True,
        blank=True,
        help_text="URL de la Norma")
    importancia_para_chile = models.ImageField("Importancia para Chile",
        upload_to='iconostemas/',
        null=True,
        blank=True,
        help_text="¿Cuán importante es este artículo(s) para la calidad de vida de las personas en Chile?")
    razones_importancia_norma = models.TextField("Razones de importancia de norma",
        null=True,
        blank=True,
        help_text="¿Por qué este artículo(s) tiene la importancia para la calidad de vida que indicaste en la pregunta anterior?")
    mejora_de_cp80 = models.ImageField("Mejora de constitución anterior",
        upload_to='iconostemas/', 
        null=True,
        blank=True,
        help_text="En el marco de una agenda de justicia social, económica y de derechos humanos: ¿en qué medida la Nueva Constitución mejora respecto de la Constitución actualmente vigente?")
    razones_mejora_cp80 = models.TextField("Razones de mejora de constitución anterior",
        null=True,
        blank=True,
        help_text="¿Cómo puedes justificar la opción asignada en la pregunta anterior?")
    presencia_otros_paises = models.TextField("Presencia en otros países",
        null=True,
        blank=True,
        help_text="¿Hay presencia de artículos similares en otros países? Explícanos en qué países y en qué se parecen")
    historia_norma = models.TextField("Historia de la norma",
        null=True,
        blank=True,
        help_text="¿Cuál es la historia de este artículo en términos de su creación social?")
    mitos_norma = models.TextField("Mitos de la norma",
        null=True,
        blank=True,
        help_text="¿Cuáles son los principales mitos asociados al artículo(s) y porqué son mitos?")
    futurista_norma = models.TextField("Futuro de la norma",
        null=True,
        blank=True,
        help_text="Imagina que estamos en 2052: ¿Cómo es tu entorno y la vida de las personas en Chile después de este artículo(s)?")
    aporte_desarrollo = models.TextField("Aporte al desarrollo",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta al desarrollo del país?")
    aporte_ddhh_natura = models.TextField("Aporte DDHH y naturaleza",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta al respeto a los derechos humanos y de la naturaleza?")
    aporte_seguridad = models.TextField("Aporte seguridad y certeza",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a la seguridad y certeza de las personas en Chile?")
    aporte_igualdad = models.TextField("Aporte a la igualdad",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a la igualdad entre todas las personas?")
    aporte_innovacion = models.TextField("Aporte a la innovación y sustentabilidad",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a la innovación y sustentabilidad?")
    aporte_descentralizacion = models.TextField("Aporte a la descentralización",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a los procesos de descentralización?")
    aporte_contra_corrupcion = models.TextField("Aporte contra la corrupción",
        null=True,
        blank=True,
        help_text="¿En qué forma el artículo(s) analizado aporta a los procesos de participación y a la lucha contra la corrupción?")
    sello_norma = models.ImageField("Imagen/Sello de Norma", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
    def __str__(self):
        return self.titulo_web_norma
