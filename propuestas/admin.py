from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import TemaPropuesta, SubtemaPropuesta, ComponenteConstitucion, Propuesta, ApoyoPropuesta, CompromisoPropuesta
from usuarios.models import User



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
    class Meta:
        model = Propuesta
        fields = ('created','modified','autor','pais','region','comuna','tema','otros_temas','tema_extra','problema','situacion','componente','otras_organizaciones','organizaciones_de_propuesta','compromiso_convencionales','anexo_propuesta','anexo2_propuesta','anexo3_propuesta','link_extra1','link_extra2','titulo','apoyos','compromisos',)


class ApoyoPropuestaAdmin(admin.ModelAdmin):
    list_display = ('propuesta', 'user')


class CompromisoPropuestaAdmin(admin.ModelAdmin):
    list_display = ('propuesta', 'user')


class TemaAdmin(ImportExportModelAdmin):
    resource_class = TemaResource


class SubtemaAdmin(ImportExportModelAdmin):
    resource_class = SubtemaResource


class PropuestaExport(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PropuestaResource


admin.site.register(TemaPropuesta, TemaAdmin)
admin.site.register(SubtemaPropuesta, SubtemaAdmin)
admin.site.register(ComponenteConstitucion)
admin.site.register(Propuesta, PropuestaExport)
admin.site.register(ApoyoPropuesta, ApoyoPropuestaAdmin)
admin.site.register(CompromisoPropuesta, CompromisoPropuestaAdmin)
