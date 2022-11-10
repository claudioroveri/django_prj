import this
from django.db import models


# Aqui ficam os modelos ORM
class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    #marca = models.CharField(max_length=50)
    marca = models.ForeignKey('Marca',on_delete=models.CASCADE)
    ano = models.IntegerField()
    automatico = models.BooleanField(default=True)