# Generated by Django 3.2.6 on 2021-08-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propuestas', '0005_auto_20210820_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubtemaPropuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtema_propuesta', models.CharField(help_text='Subtemas predefinidos de propuestas', max_length=100, unique=True, verbose_name='Subtema de Propuesta')),
                ('icono_tema', models.ImageField(blank=True, null=True, upload_to='iconostemas/', verbose_name='Ícono Temas Propuestas')),
            ],
            options={
                'verbose_name': 'Subtema Propuestas',
                'verbose_name_plural': 'Subtemas Propuestas',
            },
        ),
        migrations.AlterField(
            model_name='propuesta',
            name='otros_temas',
            field=models.ManyToManyField(blank=True, related_name='otros_temas_propuesta', to='propuestas.SubtemaPropuesta', verbose_name='Otros Temas de Propuesta'),
        ),
    ]
