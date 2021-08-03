from django.urls import path
from . import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('ciudadano_register/',views.ciudadano_register.as_view(), name='ciudadano_register'),
     path('organizacion_register/',views.organizacion_register.as_view(), name='organizacion_register'),
     path('convencional_register/',views.convencional_register.as_view(), name='convencional_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]
