# Generated by Django 4.2.7 on 2024-02-14 21:01

import comunidad.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0013_remove_usuario_rol_alter_usuario_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('AD', 'Administrador'), ('CL', 'Cliente'), ('TE', 'Tendero')], default='CL', max_length=2, verbose_name='Rol'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, default='comunidad/default-user.jpg', null=True, upload_to=comunidad.models.get_image_filename),
        ),
    ]
