# Generated by Django 3.0.6 on 2020-05-14 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_auto_20200514_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='usuarioActual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.Usuario'),
        ),
    ]
