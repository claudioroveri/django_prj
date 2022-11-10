from django.forms import ModelForm
from app.model.Marca import Marca 

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['descricao', 'origem', 'luxo']