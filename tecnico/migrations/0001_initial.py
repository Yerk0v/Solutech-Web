# Generated by Django 3.2.8 on 2021-12-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registroTecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=100)),
            ],
        ),
    ]
