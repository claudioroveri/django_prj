import this
from django.db import models

# Modelo Cliente utilizado na aula de Python
# Atributo usuario é "chave estrangeira" para o classe Usuario x
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    idade = models.IntegerField()
    ativo = models.BooleanField(default=True)
    usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE, default=1)