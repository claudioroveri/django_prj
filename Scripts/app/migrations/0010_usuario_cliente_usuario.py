# Generated by Django 4.1.1 on 2022-10-24 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]
