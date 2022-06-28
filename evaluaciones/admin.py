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
    # org_evaluadora = fields.Field(attribute='org_evaluadora', widget=ForeignKeyWidget(OrganizacionNorma, field='org_evaluadora'), column_name='org_evaluadora')
    # categoriadelanorma = fields.Field(attribute='categoriadelanorma', widget=ForeignKeyWidget(CategoriaNorma, field='categoriadelanorma'), column_name='categoriadelanorma')
    # tags_norma = fields.Field(attribute='tags_norma', widget=ManyToManyWidget(TagNorma, field='tags_norma'), column_name='tags_norma')
    titulo_oficial_norma = fields.Field(attribute='titulo_oficial_norma', column_name='titulo_oficial_norma')
    titulo_web_norma = fields.Field(attribute='titulo_web_norma', column_name='titulo_web_norma')
    resumen_norma = fields.Field(attribute='resumen_norma', column_name='resumen_norma')
    url = fields.Field(attribute='url', column_name='url')
    importancia_para_chile = fields.Field(attribute='importancia_para_chile', column_name='importancia_para_chile')
    razones_importancia_norma = fields.Field(attribute='razones_importancia_norma', column_name='razones_importancia_norma')
    mejora_de_cp80 = fields.Field(attribute='mejora_de_cp80', column_name='mejora_de_cp80')
    razones_mejora_cp80 = fields.Field(attribute='razones_mejora_cp80', column_name='razones_mejora_cp80')
    presencia_otros_paises = fields.Field(attribute='presencia_otros_paises', column_name='presencia_otros_paises')
    historia_norma = fields.Field(attribute='historia_norma', column_name='historia_norma')
    mitos_norma = fields.Field(attribute='mitos_norma', column_name='mitos_norma')
    futurista_norma = fields.Field(attribute='futurista_norma', column_name='futurista_norma')
    aporte_desarrollo = fields.Field(attribute='aporte_desarrollo', column_name='aporte_desarrollo')
    aporte_ddhh_natura = fields.Field(attribute='aporte_ddhh_natura', column_name='aporte_ddhh_natura')
    aporte_seguridad = fields.Field(attribute='aporte_seguridad', column_name='aporte_seguridad')
    aporte_igualdad = fields.Field(attribute='aporte_igualdad', column_name='aporte_igualdad')
    aporte_innovacion = fields.Field(attribute='aporte_innovacion', column_name='aporte_innovacion')
    aporte_descentralizacion = fields.Field(attribute='aporte_descentralizacion', column_name='aporte_descentralizacion')
    aporte_contra_corrupcion = fields.Field(attribute='aporte_contra_corrupcion', column_name='aporte_contra_corrupcion')
    anexo_norma_pdf = fields.Field(attribute='anexo_norma_pdf', column_name='anexo_norma_pdf')
    anexo_norma_png = fields.Field(attribute='anexo_norma_png', column_name='anexo_norma_png')
    sello_norma = fields.Field(attribute='sello_norma', column_name='sello_norma')
    # prev_norma = fields.Field(attribute='prev_norma', widget=ForeignKeyWidget(Norma, field='prev_norma'), column_name='prev_norma')
    # next_norma = fields.Field(attribute='next_norma', widget=ForeignKeyWidget(Norma, field='next_norma'), column_name='next_norma')

    class Meta:
        model = Norma
        import_id_fields = ('id',)
        exclude = ('prev_norma','next_norma',)


class OrganizacionNormaAdmin(ImportExportModelAdmin):
    resource_class = OrganizacionNormaResource

class CategoriaNormaAdmin(ImportExportModelAdmin):
    resource_class = CategoriaNormaResource

class TagNormaAdmin(ImportExportModelAdmin):
    resource_class = TagNormaResource

class NormaAdmin(ImportExportModelAdmin):
    resource_class = NormaResource


admin.site.register(OrganizacionNorma, OrganizacionNormaAdmin)
admin.site.register(CategoriaNorma, CategoriaNormaAdmin)
admin.site.register(TagNorma, TagNormaAdmin)
admin.site.register(Norma, NormaAdmin)
