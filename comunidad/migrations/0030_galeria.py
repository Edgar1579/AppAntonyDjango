# Generated by Django 4.2.7 on 2024-02-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0029_remove_usuario_rol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotos', models.ImageField(upload_to='fotos')),
                ('videos', models.FileField(upload_to='videos')),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]