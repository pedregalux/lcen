# Generated by Django 3.2.6 on 2021-09-11 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propuestas', '0007_auto_20210907_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propuesta',
            name='convencionales_comprometidos',
        ),
    ]
