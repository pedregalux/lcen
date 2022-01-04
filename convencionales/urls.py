from django.urls import path
from . import views
from .views import *
from convencionales.views import *


urlpatterns=[
    path('verconvencionales/', views.VerConvencionalesView.as_view(), name='ver_convencionales'),
    path('verconvencionales/<pk>', views.VerConvencionalView.as_view(), name='ver_convencional'),
]
