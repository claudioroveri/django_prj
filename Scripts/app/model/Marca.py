import this
from django.db import models

class Marca(models.Model):
    descricao = models.CharField(max_length=50)
    origem = models.CharField(max_length=50)
    luxo = models.BooleanField(default=False)