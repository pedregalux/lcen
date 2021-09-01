from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static



admin.site.site_header = 'LCeN'                    # default: "Django Administration"
admin.site.index_title = 'La Constitución es Nuestra Admin'  # default: "Site administration"
admin.site.site_title = 'La Constitución es Nuestra Admin' # default: "Django site admin"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('accounts/', include('allauth.urls')),
    path('propuestas/', include('propuestas.urls')),
    path('convencionales/', include('convencionales.urls')),
    path('organizaciones/', include('organizaciones.urls')),
    path('laconstitucion/', include('laconstitucion.urls')),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}, name='static'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
