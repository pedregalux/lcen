from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import OrganizacionNorma,CategoriaNorma,TagNorma,Norma


class OrganizacionNormaResource(resources.ModelResource):
    class Meta:
        model = OrganizacionNorma
        import_id_fields = ('id',)
        fields = ('id','nombre_org_norma','logo_org_norma',)


class CategoriaNormaResource(resources.ModelResource):
    class Meta:
        model = CategoriaNorma
        import_id_fields = ('id',)
        fields = ('id','tema_norma',)


class TagNormaResource(resources.ModelResource):
    class Meta:
        model = TagNorma
        import_id_fields = ('id',)
        fields = ('id','tag_norma','icono_tag',)


class NormaResource(resources.ModelResource):
    org_evaluadora = fields.Field(attribute='org_evaluadora', widget=ForeignKeyWidget(OrganizacionNorma, field='org_evaluadora'), column_name='org_evaluadora')
    categoriadelanorma = fields.Field(attribute='categoriadelanorma', widget=ForeignKeyWidget(CategoriaNorma, field='categoriadelanorma'), column_name='categoriadelanorma')
    tags_norma = fields.Field(attribute='tags_norma', widget=ManyToManyWidget(TagNorma, field='tags_norma'), column_name='tags_norma')
    titulo_oficial_norma = fields.Field(attribute='titulo_oficial_norma', column_name='titulo_oficial_norma')
    titulo_web_norma = fields.Field(attribute='titulo_web_norma', column_name='titulo_web_norma')
    resumen_norma = fields.Field(attribute='resumen_norma', column_name='resumen_norma')
    url = fields.Field(attribute='url', column_name='url')
    importancia_para_chile = fields.Field(attribute='importancia_para_chile', column_name='importancia_para_chile')
    razones_importancia_norma = fields.Field(attribute='razones_importancia_norma', column_name='razones_importancia_norma')
    mejora_de_cp80 = fields.Field(attribute='mejora_de_cp80', column_name='mejora_de_cp80')
    razones_mejora_cp80 = fields.Field(attribute='razones_mejora_cp80', column_name='razones_mejora_cp80')
    tema_extra = fields.Field(attribute='tema_extra', column_name='Tema')
    tema_extra = fields.Field(attribute='tema_extra', column_name='Tema')
    tema_extra = fields.Field(attribute='tema_extra', column_name='Tema')


    class Meta:
        model = Norma
        import_id_fields = ('id',)
        fields = ('id','nombre_org_norma','logo_org_norma',)



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
    anexo_norma_pdf = models.FileField(upload_to='documents/',
        verbose_name="Documento del artículo",
        null=True,
        blank=True)
    anexo_norma_png = models.FileField(upload_to='documents/',
        verbose_name="Ilustración del artículo",
        null=True,
        blank=True)
    sello_norma = models.ImageField("Imagen/Sello de Norma", upload_to='iconostemas/', null=True, blank=True)
    prev_norma = models.ForeignKey("self", related_name="norma_prev", null=True, blank=True, on_delete=models.CASCADE)
    next_norma = models.ForeignKey("self", related_name="norma_next", null=True, blank=True, on_delete=models.CASCADE)









class OrganizacionNormaAdmin(ImportExportModelAdmin):
    resource_class = OrganizacionNormaResource


class CategoriaNormaAdmin(ImportExportModelAdmin):
    resource_class = CategoriaNormaResource


class TagNormaAdmin(ImportExportModelAdmin):
    resource_class = TagNormaResource

admin.site.register(OrganizacionNorma, OrganizacionNormaAdmin)
admin.site.register(CategoriaNorma, CategoriaNormaAdmin)
admin.site.register(TagNorma, TagNormaAdmin)
admin.site.register(Norma)
