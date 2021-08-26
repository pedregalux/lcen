from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User, Ciudadano, Organizacion, Convencional


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UserAdmin(UserAdmin):
    form = UserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('nombre','is_ciudadano','is_organizacion','is_convencional',)}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Ciudadano)
admin.site.register(Organizacion)
admin.site.register(Convencional)
