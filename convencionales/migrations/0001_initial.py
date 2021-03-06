# Generated by Django 3.2.6 on 2021-08-16 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mantenedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=220, unique=True, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=220, unique=True, verbose_name='Nombre Lista')),
            ],
            options={
                'verbose_name': 'Lista',
                'verbose_name_plural': 'Listas',
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True, verbose_name='Nombre Partido/Movimiento')),
                ('sigla', models.CharField(max_length=50, unique=True, verbose_name='Sigla Partido/Movimiento')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/', verbose_name='Logo Partido/Movimiento')),
            ],
            options={
                'verbose_name': 'Partido/Movimiento',
                'verbose_name_plural': 'Partidos/Movimientos',
            },
        ),
        migrations.CreateModel(
            name='Constituyente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True, verbose_name='Nombre Constituyente')),
                ('linkintereses', models.URLField(blank=True, max_length=225, null=True, verbose_name='Link Declaraci??n de Intereses')),
                ('biografia', models.TextField(blank=True, null=True, verbose_name='Historia Pol??tica')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail de Contacto')),
                ('twitter', models.URLField(blank=True, max_length=254, null=True, verbose_name='Twitter')),
                ('facebook', models.URLField(blank=True, max_length=254, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, max_length=254, null=True, verbose_name='Instagram')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_constituyentes/', verbose_name='Foto Constituyente')),
                ('cargo', models.ManyToManyField(blank=True, related_name='cargos_constituyente', to='convencionales.Cargo', verbose_name='Cargos de Constituyente en la Convenci??n')),
                ('distrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distrito_constituyente', to='mantenedores.distrito', verbose_name='Distrito del Constituyente')),
                ('lista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lista_constituyente', to='convencionales.lista', verbose_name='Lista del Constituyente')),
                ('movimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movimiento_constituyente', to='convencionales.movimiento', verbose_name='Partido/Movimiento del Constituyente')),
            ],
            options={
                'verbose_name': 'Constituyente',
                'verbose_name_plural': 'Constituyentes',
            },
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=220, unique=True, verbose_name='Nombre Comisi??n')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descipci??n de la Comisi??n')),
                ('integrantes', models.ManyToManyField(blank=True, related_name='integrantes_comision', to='convencionales.Constituyente', verbose_name='Integrantes de la Comisi??n')),
                ('presidentes', models.ManyToManyField(blank=True, related_name='presidentes_comision', to='convencionales.Constituyente', verbose_name='President@(s) de la Comisi??n')),
            ],
            options={
                'verbose_name': 'Comisi??n',
                'verbose_name_plural': 'Comisiones',
            },
        ),
    ]
