from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import User, Ciudadano, Organizacion, Convencional



class UserResource(resources.ModelResource):
    class Meta:
        model = User
        exclude = ('password','groups','user_permissions',)


class CiudadanoResource(resources.ModelResource):
    user = fields.Field(attribute='user', widget=ForeignKeyWidget(User, field='username'),column_name='Usuario')

    class Meta:
        model = Ciudadano
        exclude = ('cualquiercosa',)


class OrganizacionResource(resources.ModelResource):
    user = fields.Field(attribute='user', widget=ForeignKeyWidget(User, field='username'),column_name='Usuario')

    class Meta:
        model = Organizacion


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UserAdmin(UserAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    form = UserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('nombre','is_ciudadano','is_organizacion','is_convencional',)}),
    )


class CiudadanoAdmin(ImportExportModelAdmin):
    resource_class = CiudadanoResource


class OrganizacionAdmin(ImportExportModelAdmin):
    resource_class = OrganizacionResource


admin.site.register(User, UserAdmin)
admin.site.register(Ciudadano, CiudadanoAdmin)
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Convencional)
