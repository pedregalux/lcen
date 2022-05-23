from django.db import models



# Es la categoría general que agrupa normas, ej: Equidad de Género, etc
class CategoriaNorma(models.Model):
    tema_norma = models.CharField("Categoría de Norma",
        max_length=100,
        unique=True,
        help_text="Categoría de la norma")
    icono_categoria = models.ImageField("Ícono Categoría Norma", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Categoría Normas"
        verbose_name_plural = "Categorías Normas"
    def __str__(self):
        return self.tema_norma


# La clase TagNorma es la que está asociada con el sello de cálidad
class TagNorma(models.Model):
    tag_norma = models.CharField("Tag de Norma",
        max_length=100,
        unique=True,
        help_text="Tag de la norma")
    icono_tag = models.ImageField("Ícono Tag Norma", upload_to='iconostemas/', null=True, blank=True)
    class Meta:
        verbose_name = "Tag Norma"
        verbose_name_plural = "Tag Normas"
    def __str__(self):
        return self.tag_norma

# La norma
class Norma(models.Model):
    titulo_oficial_norma = models.TextField("Título oficial de norma",
        unique=True,
        help_text="Título oficial de la norma")
    titulo_web_norma = models.CharField("Título web de la norma",
        max_length=256,
        unique=True,
        help_text="Título oficial de la norma")
    resumen_norma = models.CharField("Resumen de la norma",
        max_length=256,
        unique=True,
        help_text="Resumen de la norma")
    sello_norma = models.ImageField("Sello de Norma", upload_to='iconostemas/', null=True, blank=True)
