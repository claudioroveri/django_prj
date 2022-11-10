from rest_framework import serializers
from app.model.Carros import Carros
from app.model.Marca import  Marca
from app.model.Usuario import Usuario

# Classe que serve para simplificar a estrutura 
# da classe Model
class CarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carros
        fields = ['id','marca', 'modelo', 'ano', 'automatico']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id','descricao', 'origem', 'luxo']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'senha']