# Generated by Django 4.1.1 on 2022-09-30 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_carros_ano2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carros',
            name='ano2',
        ),
    ]