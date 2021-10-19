from django.db import models
from mantenedores.models import Distrito



class Cargo(models.Model):
    nombre = models.CharField("Cargo", max_length=220, unique=True)
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
    def __str__(self):
        return self.nombre



class Lista(models.Model):
    nombre = models.CharField("Nombre Colectivo", max_length=220, unique=True)
    class Meta:
        verbose_name = "Colectivo"
        verbose_name_plural = "Colectivos"
    def __str__(self):
        return self.nombre



class Movimiento(models.Model):
    nombre = models.CharField("Nombre Partido/Movimiento", max_length=255, unique=True)
    sigla = models.CharField("Sigla Partido/Movimiento", max_length=50, unique=True)
    logo = models.ImageField("Logo Partido/Movimiento", upload_to='logos/', null=True, blank=True)
    class Meta:
        verbose_name = "Partido/Movimiento"
        verbose_name_plural = "Partidos/Movimientos"
    def __str__(self):
        return self.nombre



class Constituyente(models.Model):
    nombre = models.CharField("Nombre Constituyente", max_length=255, unique=True)
    cargo = models.ManyToManyField(Cargo, related_name="cargos_constituyente", verbose_name="Cargos de Constituyente en la Convención", blank=True)
    lista = models.ForeignKey(Lista, related_name="lista_constituyente", verbose_name="Lista del Constituyente", null=True, blank=True, on_delete=models.SET_NULL)
    distrito = models.ForeignKey(Distrito, related_name="distrito_constituyente", verbose_name="Distrito del Constituyente", null=True, blank=True, on_delete=models.SET_NULL)
    movimiento = models.ForeignKey(Movimiento, related_name="movimiento_constituyente", verbose_name="Partido/Movimiento del Constituyente", null=True, blank=True, on_delete=models.SET_NULL)
    linkintereses = models.URLField("Link Declaración de Intereses", max_length = 225, null=True, blank=True)
    biografia = models.TextField("Historia Política", null=True, blank=True)
    email = models.EmailField("E-mail de Contacto", max_length=254, null=True, blank=True)
    twitter = models.URLField("Twitter", max_length=254, null=True, blank=True)
    facebook = models.URLField("Facebook", max_length=254, null=True, blank=True)
    instagram = models.URLField("Instagram", max_length=254, null=True, blank=True)
    foto = models.ImageField("Foto Constituyente", upload_to='fotos_constituyentes/', null=True, blank=True)
    class Meta:
        verbose_name = "Constituyente"
        verbose_name_plural = "Constituyentes"
    def __str__(self):
        return self.nombre
    def display_cargo(self):
        return ', '.join([ cargo.nombre for cargo in self.cargo.all()[:3] ])



class Comision(models.Model):
    nombre = models.CharField("Nombre Comisión", max_length=220, unique=True)
    descripcion = models.TextField("Descipción de la Comisión", blank=True, null=True)
    presidentes = models.ManyToManyField(Constituyente, related_name="presidentes_comision", verbose_name="President@(s) de la Comisión", blank=True)
    integrantes = models.ManyToManyField(Constituyente, related_name="integrantes_comision", verbose_name="Integrantes de la Comisión", blank=True)
    class Meta:
        verbose_name = "Comisión"
        verbose_name_plural = "Comisiones"
    def __str__(self):
        return self.nombre
