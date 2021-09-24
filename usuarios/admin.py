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
        exclude = ('password','groups',)


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UserAdmin(UserAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    form = UserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('nombre','is_ciudadano','is_organizacion','is_convencional',)}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Ciudadano)
admin.site.register(Organizacion)
admin.site.register(Convencional)
