# Generated by Django 3.2.9 on 2022-05-20 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convencionales', '0002_auto_20220520_1244'),
        ('usuarios', '0011_auto_20210909_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convencional',
            name='lista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lista_de_constituyente', to='convencionales.lista', verbose_name='Colectivo del Constituyente'),
        ),
    ]
