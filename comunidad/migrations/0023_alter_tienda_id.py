# Generated by Django 4.2.7 on 2024-02-15 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0022_tienda_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]