# Generated by Django 5.0.3 on 2024-03-28 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0015_rename_tienda_foto_fotos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foto',
            old_name='fotos',
            new_name='tienda',
        ),
    ]