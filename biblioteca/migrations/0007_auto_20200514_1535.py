# Generated by Django 3.0.6 on 2020-05-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_auto_20200514_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejemplar',
            name='usuarioActual',
        ),
        migrations.AddField(
            model_name='usuario',
            name='ejemplares',
            field=models.ManyToManyField(to='biblioteca.Ejemplar'),
        ),
    ]