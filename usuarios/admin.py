from django.contrib import admin
from .models import User, Ciudadano, Organizacion, Convencional

admin.site.register(User)
admin.site.register(Ciudadano)
admin.site.register(Organizacion)
admin.site.register(Convencional)
