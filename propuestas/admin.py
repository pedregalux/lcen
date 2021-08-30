from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import TemaPropuesta, SubtemaPropuesta, ComponenteConstitucion, Propuesta, ApoyoPropuesta, CompromisoPropuesta



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


class ApoyoPropuestaAdmin(admin.ModelAdmin):
    list_display = ('propuesta', 'user')


class CompromisoPropuestaAdmin(admin.ModelAdmin):
    list_display = ('propuesta', 'user')


class TemaAdmin(ImportExportModelAdmin):
    resource_class = TemaResource


class SubtemaAdmin(ImportExportModelAdmin):
    resource_class = SubtemaResource


admin.site.register(TemaPropuesta, TemaAdmin)
admin.site.register(SubtemaPropuesta, SubtemaAdmin)
admin.site.register(ComponenteConstitucion)
admin.site.register(Propuesta)
admin.site.register(ApoyoPropuesta, ApoyoPropuestaAdmin)
admin.site.register(CompromisoPropuesta, CompromisoPropuestaAdmin)
