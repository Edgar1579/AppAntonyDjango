# Generated by Django 4.2.7 on 2024-02-14 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0016_tienda_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tienda',
            name='usuario',
        ),
    ]
