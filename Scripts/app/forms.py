from django.forms import ModelForm
from app.models import Carros, Marca, Cliente, Usuario
from django.contrib.auth.models import User

# Aqui são criados os Beans para os formularios
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['id','modelo', 'marca', 'ano', 'automatico']

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['descricao', 'origem', 'luxo']

# Classe necessária para vincular ao formulário HTML (como se fosse um Javabean)
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'senha']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'idade', 'ativo']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name','last_name', 'password']




