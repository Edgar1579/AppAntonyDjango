# Generated by Django 5.0.3 on 2024-03-28 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0014_foto_tienda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foto',
            old_name='tienda',
            new_name='fotos',
        ),
    ]
