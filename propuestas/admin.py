from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import TemaPropuesta, SubtemaPropuesta, ComponenteConstitucion, Propuesta, ApoyoPropuesta, CompromisoPropuesta
from usuarios.models import User
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
        titulo = fields.Field(attribute='titulo', column_name='Título')
        tema = fields.Field(attribute='tema', widget=ForeignKeyWidget(SubtemaPropuesta, field='subtema_propuesta'), column_name='Tema Principal')
        otros_temas = fields.Field(attribute='otros_temas', widget=ManyToManyWidget(SubtemaPropuesta, field='subtema_propuesta'), column_name='Sub Temas')
        tema_extra = fields.Field(attribute='tema_extra', column_name='Tema Extra')


        class Meta:
            model = Propuesta
            fields = ('created','modified','autor','pais','region','comuna','tema_extra','problema','situacion','componente','otras_organizaciones','organizaciones_de_propuesta','compromiso_convencionales','anexo_propuesta','anexo2_propuesta','anexo3_propuesta','link_extra1','link_extra2','titulo','apoyos','compromisos',)


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
