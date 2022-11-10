from django.forms import ModelForm
from app.model.Usuario import Usuario

# Classe necessária para vincular ao formulário HTML (como se fosse um Javabean)
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'senha']