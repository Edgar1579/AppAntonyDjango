# Generated by Django 4.2.7 on 2023-11-12 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0003_usuario_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='primerprimer_nombre',
            new_name='primer_nombre',
        ),
    ]
