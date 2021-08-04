from django.urls import path
from . import  views



urlpatterns=[
    path('verorganizaciones/',views.VerOrganizacionesView.as_view(), name='verorganizaciones'),
    path('verorganizaciones/<pk>',views.VerOrganizacionView.as_view(), name='verorganizacion'),
    path('crearorganizaciones/',views.CrearOrganizacionView.as_view(), name='crearorganizacion'),
    path('cambiarorganizaciones/',views.CambiarOrganizacionView.as_view(), name='cambiarorganizacion'),
]
