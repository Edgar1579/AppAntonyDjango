# Generated by Django 5.0.3 on 2024-03-28 17:32

import operaciones.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0011_foto_tienda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default='operaciones/productos/default-product.png', null=True, upload_to=operaciones.models.get_image_filename),
        ),
    ]