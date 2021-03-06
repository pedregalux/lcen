# Generated by Django 3.2.6 on 2021-08-16 21:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mantenedores', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_ciudadano', models.BooleanField(default=False)),
                ('is_organizacion', models.BooleanField(default=False)),
                ('is_convencional', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('email_contacto', models.EmailField(max_length=255)),
                ('telefono_contacto', models.CharField(max_length=255)),
                ('cualquiercosa', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Organzaci??n',
                'verbose_name_plural': 'Organizaciones',
            },
        ),
        migrations.CreateModel(
            name='Convencional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('cualquiercosa', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Convencional',
                'verbose_name_plural': 'Convencionales',
            },
        ),
        migrations.CreateModel(
            name='Ciudadano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('genero', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino'), ('No Binario', 'No Binario'), ('No Declara', 'No Declara')], max_length=100, verbose_name='G??nero')),
                ('rangoedad', models.CharField(choices=[('-20', '-20'), ('20-29', '20-29'), ('30-39', '30-39'), ('40-49', '40-49'), ('50-59', '50-59'), ('60-69', '60-69'), ('70+', '70+'), ('No Declara', 'No Declara')], max_length=100, verbose_name='Rango Edad')),
                ('cualquiercosa', models.CharField(max_length=255)),
                ('comuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedores.comuna')),
                ('pais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedores.pais')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedores.region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ciudadan@',
                'verbose_name_plural': 'Ciudadan@s',
            },
        ),
    ]
