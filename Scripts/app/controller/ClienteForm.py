from django.forms import ModelForm
from app.model.Cliente import Cliente 

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'idade', 'ativo', 'usuario']