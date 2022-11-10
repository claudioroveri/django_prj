#import this
#from django.db import models


# Aqui ficam os modelos ORM
#class Carros(models.Model):
#    modelo = models.CharField(max_length=150)
#    #marca = models.CharField(max_length=50)
#    marca = models.ForeignKey('Marca',on_delete=models.CASCADE)
#    ano = models.IntegerField()
#    automatico = models.BooleanField(default=True)
      
#class Marca(models.Model):
#    descricao = models.CharField(max_length=50)
#    origem = models.CharField(max_length=50)
#    luxo = models.BooleanField(default=False)

# Modelo Cliente utilizado na aula de Python
# Atributo usuario é "chave estrangeira" para o classe Usuario x
#class Cliente(models.Model):
#    nome = models.CharField(max_length=100)
#    endereco = models.CharField(max_length=200)
#    idade = models.IntegerField()
#    ativo = models.BooleanField(default=True)
#    usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE, default=1)

##class Usuario(models.Model):
#    email = models.CharField(max_length=50)
#    senha = models.CharField(max_length=20)

