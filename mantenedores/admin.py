from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Pais, Region, Distrito, Comuna, Alcance


class PaisResource(resources.ModelResource):
    class Meta:
        model = Pais
        import_id_fields = ('id',)
        fields = ('id','pais',)


class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
        import_id_fields = ('id',)
        fields = ('id','region',)


class DistritoResource(resources.ModelResource):
    class Meta:
        model = Distrito
        import_id_fields = ('id',)
        fields = ('id','distrito','region_distrito',)


class ComunaResource(resources.ModelResource):
    class Meta:
        model = Comuna
        import_id_fields = ('id',)
        fields = ('id','comuna','distrito_comuna',)


class PaisAdmin(ImportExportModelAdmin):
    resource_class = PaisResource


class RegionAdmin(ImportExportModelAdmin):
    resource_class = RegionResource


class DistritoAdmin(ImportExportModelAdmin):
    resource_class = DistritoResource


class ComunaAdmin(ImportExportModelAdmin):
    resource_class = ComunaResource


admin.site.register(Pais, PaisAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Distrito, DistritoAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Alcance)
