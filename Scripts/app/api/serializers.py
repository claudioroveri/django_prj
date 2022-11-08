from rest_framework import serializers
from app.models import Carros, Marca, Usuario

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