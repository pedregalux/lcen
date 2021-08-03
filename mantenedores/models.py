from django.db import models



class Pais(models.Model):
    pais = models.CharField("País",
        max_length=225,
        unique=True)
    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
    def __str__(self):
        return self.pais



class Region(models.Model):
    region = models.CharField("Región",
        max_length=225,
        unique=True)
    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
    def __str__(self):
        return self.region



class Distrito(models.Model):
    distrito = models.CharField("Distrito",
        max_length=225,
        unique=True)
    region_distrito = models.ForeignKey(Region,
        related_name="region_distrito",
        verbose_name="Región del Distrito",
        null=True,
        on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Distrito"
        verbose_name_plural = "Distritos"
    def __str__(self):
        return self.distrito



class Comuna(models.Model):
    comuna = models.CharField("Comuna",
        max_length=225,
        unique=True)
    distrito_comuna = models.ForeignKey(Distrito,
        related_name="distrito_comuna",
        verbose_name="Distrito de la Comuna",
        null=True,
        on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"
    def __str__(self):
        return self.comuna



class Alcance(models.Model):
    alcance = models.CharField("Alcance",
        max_length=225,
        unique=True)
    class Meta:
        verbose_name = "Alcance"
        verbose_name_plural = "Alcances"
    def __str__(self):
        return self.alcance
