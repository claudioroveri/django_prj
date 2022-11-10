from django.forms import ModelForm
from app.model.Carros import Carros

# Aqui são criados os Beans para os formularios
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['id','modelo', 'marca', 'ano', 'automatico']