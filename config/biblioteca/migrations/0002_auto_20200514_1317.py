# Generated by Django 3.0.6 on 2020-05-14 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Autor'),
        ),
    ]