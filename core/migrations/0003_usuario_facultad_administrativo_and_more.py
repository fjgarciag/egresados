# Generated by Django 5.0 on 2023-12-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_usuario_numero_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='facultad_administrativo',
            field=models.CharField(blank=True, default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_administrativo',
            field=models.CharField(blank=True, default=False, max_length=100),
        ),
    ]
