# Generated by Django 5.0 on 2023-12-27 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='numero_celular',
        ),
    ]
