from django.shortcuts import render, redirect
from propuestas.models import Propuesta
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from propuestas.forms import CrearPropuestaForm



# class UserAccessMixin(PermissionRequiredMixin):
#     def dispatch(self, request, *args, **kwargs):
#         if (not self.request.user.is_authenticated):
#             return redirect_to_login(self.request.get_full_path(),
#                                     self.get_login_url(), self.get_redirect_field_name())
#         if not self.has_permission():
#             return redirect('login')
#         return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)



class VerPropuestasView(ListView):
    model = Propuesta
    context_object_name = 'propuestas_list'
    template_name = 'propuestas/ver_propuestas.html'



class VerPropuestaView(DetailView):
    model = Propuesta
    context_object_name = 'propuestas_detail'
    template_name = 'propuestas/ver_propuesta.html'



class CrearPropuestaView(LoginRequiredMixin, FormView):
    permission_required = 'propuestas.add_propuesta'
    form_class = CrearPropuestaForm
    template_name = 'propuestas/crear_propuesta.html'
    success_url = '/propuestas/'
    login_url = 'login'
    def form_valid(self, form):
        if form.is_valid():
            prop = form.save(commit=False)
            prop.autor = self.request.user
            form.save()
        return super().form_valid(form)



# class CrearPropuestaView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
#     permission_required = 'propuestas.add_propuesta'
#     form_class = CrearPropuestaForm
#     template_name = 'propuestas/crear_propuesta.html'
#     success_url = '/propuestas/'
#     login_url = 'login'
#     def form_valid(self, form):
#         if form.is_valid():
#             prop = form.save(commit=False)
#             prop.autor = self.request.user
#             form.save()
#         return super().form_valid(form)
