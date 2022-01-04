from django.contrib import admin
from .models import Cargo, Lista, Movimiento, Comision, Constituyente

admin.site.register(Constituyente)
admin.site.register(Cargo)
admin.site.register(Lista)
admin.site.register(Movimiento)
admin.site.register(Comision)
