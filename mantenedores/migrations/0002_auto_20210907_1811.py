# Generated by Django 3.2.6 on 2021-09-07 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comuna',
            options={'ordering': ['comuna'], 'verbose_name': 'Comuna', 'verbose_name_plural': 'Comunas'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'ordering': ['pais'], 'verbose_name': 'País', 'verbose_name_plural': 'Países'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['region'], 'verbose_name': 'Región', 'verbose_name_plural': 'Regiones'},
        ),
    ]
