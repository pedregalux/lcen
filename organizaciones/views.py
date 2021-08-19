from django.shortcuts import render, redirect
from organizaciones.models import OrganizacionProfile
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin



# class VerOrganizacionesView(ListView):
#     model = OrganizacionProfile
#     context_object_name = 'organizaciones_list'
#     template_name = 'organizaciones/ver_organizaciones.html'
#
#
#
# class VerOrganizacionView(DetailView):
#     model = OrganizacionProfile
#     context_object_name = 'organizaciones_detail'
#     template_name = 'organizaciones/ver_organizacion.html'
#
#
#
# class CrearOrganizacionView(PermissionRequiredMixin, FormView):
#     pass
#
#
#
# class CambiarOrganizacionView(PermissionRequiredMixin, FormView):
#     pass
