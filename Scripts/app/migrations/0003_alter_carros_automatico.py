# Generated by Django 4.1.1 on 2022-09-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_carros_automatico_alter_carros_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='automatico',
            field=models.BooleanField(),
        ),
    ]