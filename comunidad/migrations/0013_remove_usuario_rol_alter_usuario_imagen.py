# Generated by Django 4.2.7 on 2024-02-14 21:00

import comunidad.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0012_tienda_estado_tienda_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, default='comunidad\\default-user.jpeg', null=True, upload_to=comunidad.models.get_image_filename),
        ),
    ]
