from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import TemaPropuesta, ComponenteConstitucion, Propuesta, ApoyoPropuesta, CompromisoPropuesta



class TemaResource(resources.ModelResource):
    class Meta:
        model = TemaPropuesta
        import_id_fields = ('id',)
        fields = ('id','tema_propuesta',)


class ApoyoPropuestaAdmin(admin.ModelAdmin):
    list_display = ('propuesta', 'user')


class CompromisoPropuestaAdmin(admin.ModelAdmin):
    list_display = ('propuesta', 'user')


class TemaAdmin(ImportExportModelAdmin):
    resource_class = TemaResource


admin.site.register(TemaPropuesta, TemaAdmin)
admin.site.register(ComponenteConstitucion)
admin.site.register(Propuesta)
admin.site.register(ApoyoPropuesta, ApoyoPropuestaAdmin)
admin.site.register(CompromisoPropuesta, CompromisoPropuestaAdmin)
