# Generated by Django 3.2.9 on 2021-11-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_usuario', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
