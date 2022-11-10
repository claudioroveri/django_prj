import this
from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)