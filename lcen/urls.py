from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from inicio.views import error404, error500, error400, error403
from django.conf.urls import handler404, handler500, handler403, handler400



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
    path('evaluaciones/', include('evaluaciones.urls')),
    path('evaluacionesinternacionales/', include('evaluacionesinternacionales.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'inicio.views.error404'
handler500 = 'inicio.views.error500'
handler403 = 'inicio.views.error403'
handler400 = 'inicio.views.error400'
