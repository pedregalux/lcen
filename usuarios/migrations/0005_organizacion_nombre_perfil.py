# Generated by Django 3.2.6 on 2021-08-19 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_remove_organizacion_nombre_organizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacion',
            name='nombre_perfil',
            field=models.CharField(default='null', help_text='Este es el nombre que será mostrado en el Perfil Público de la Organización en la plataforma', max_length=255, verbose_name='Nombre Perfil'),
            preserve_default=False,
        ),
    ]