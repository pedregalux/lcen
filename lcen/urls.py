from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header = 'LCeN'                    # default: "Django Administration"
admin.site.index_title = 'La Constitución es Nuestra Admin'  # default: "Site administration"
admin.site.site_title = 'La Constitución es Nuestra Admin' # default: "Django site admin"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
