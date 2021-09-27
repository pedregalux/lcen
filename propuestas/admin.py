from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import TemaPropuesta, SubtemaPropuesta, ComponenteConstitucion, Propuesta, ApoyoPropuesta, CompromisoPropuesta
from usuarios.models import User, Ciudadano, Organizacion
from mantenedores.models import *



class TemaResource(resources.ModelResource):
    class Meta:
        model = TemaPropuesta
        import_id_fields = ('id',)
        fields = ('id','tema_propuesta',)


class SubtemaResource(resources.ModelResource):
    class Meta:
        model = SubtemaPropuesta
        import_id_fields = ('id',)
        fields = ('id','subtema_propuesta',)


class PropuestaResource(resources.ModelResource):
    autor = fields.Field(attribute='autor', widget=ForeignKeyWidget(User, field='username'), column_name='Autor')
    titulo = fields.Field(attribute='titulo', column_name='Título')
    tema = fields.Field(attribute='tema', widget=ForeignKeyWidget(SubtemaPropuesta, field='tema_propuesta'), column_name='Tema Principal')
    otros_temas = fields.Field(attribute='otros_temas', widget=ManyToManyWidget(SubtemaPropuesta, field='subtema_propuesta'), column_name='Sub Temas')
    tema_extra = fields.Field(attribute='tema_extra', column_name='Tema Extra')
    pais = fields.Field(attribute='pais', widget=ForeignKeyWidget(Pais, field='pais'), column_name='País')
    region = fields.Field(attribute='region', widget=ForeignKeyWidget(Region, field='region'), column_name='Región')
    comuna = fields.Field(attribute='comuna', widget=ForeignKeyWidget(Comuna, field='comuna'), column_name='Comuna')
    problema = fields.Field(attribute='problema', column_name='Problema')
    situacion = fields.Field(attribute='situacion', column_name='Situación Ideal')
    componente = fields.Field(attribute='componente', column_name='Debe estar en la CP')
    otras_organizaciones = fields.Field(attribute='otras_organizaciones', column_name='Con o sin Orgs')
    organizaciones_de_propuesta = fields.Field(attribute='organizaciones_de_propuesta', column_name='Organizaciones')
    compromiso_convencionales = fields.Field(attribute='compromiso_convencionales', column_name='Con o sin Compromisos')
    anexo3_propuesta = fields.Field(attribute='anexo3_propuesta', column_name='Archivo Compromisos')
    anexo1_propuesta = fields.Field(attribute='anexo_propuesta', column_name='Archivo Anexo 1')
    anexo2_propuesta = fields.Field(attribute='anexo2_propuesta', column_name='Archivo Anexo 2')
    link_extra1 = fields.Field(attribute='link_extra1', column_name='Link Anexo 1')
    link_extra2 = fields.Field(attribute='link_extra2', column_name='Link Anexo 2')

    class Meta:
        model = Propuesta
        fields = ('id','created','modified','apoyos','compromisos')


class ApoyoPropuestaAdmin(admin.ModelAdmin):
    list_display = ('propuesta', 'user')


class CompromisoPropuestaAdmin(admin.ModelAdmin):
    list_display = ('propuesta', 'user')


class TemaAdmin(ImportExportModelAdmin):
    resource_class = TemaResource


class SubtemaAdmin(ImportExportModelAdmin):
    resource_class = SubtemaResource


class PropuestaExport(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('titulo', 'autor')
    resource_class = PropuestaResource


admin.site.register(TemaPropuesta, TemaAdmin)
admin.site.register(SubtemaPropuesta, SubtemaAdmin)
admin.site.register(ComponenteConstitucion)
admin.site.register(Propuesta, PropuestaExport)
admin.site.register(ApoyoPropuesta, ApoyoPropuestaAdmin)
admin.site.register(CompromisoPropuesta, CompromisoPropuestaAdmin)
