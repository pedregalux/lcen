from django.contrib import admin
from .models import TemaPropuesta, ComponenteConstitucion, Propuesta, ApoyoPropuesta



class ApoyoPropuestaAdmin(admin.ModelAdmin):
    list_display = ('propuesta', 'user')


admin.site.register(TemaPropuesta)
admin.site.register(ComponenteConstitucion)
admin.site.register(Propuesta)
admin.site.register(ApoyoPropuesta, ApoyoPropuestaAdmin)
