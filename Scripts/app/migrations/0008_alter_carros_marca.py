# Generated by Django 4.1.1 on 2022-09-30 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_carros_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.marca'),
        ),
    ]