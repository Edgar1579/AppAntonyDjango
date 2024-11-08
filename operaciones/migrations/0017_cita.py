# Generated by Django 5.0.3 on 2024-04-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0016_rename_fotos_foto_tienda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('comentarios', models.TextField(blank=True)),
            ],
        ),
    ]
