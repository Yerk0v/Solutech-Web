# Generated by Django 3.2.8 on 2021-11-28 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioTecnicoApps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='servicio',
        ),
        migrations.RemoveField(
            model_name='ordendetalle',
            name='orden',
        ),
        migrations.RemoveField(
            model_name='ordendetalle',
            name='servicio',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Orden',
        ),
        migrations.DeleteModel(
            name='OrdenDetalle',
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
    ]
