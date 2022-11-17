from django.forms import ModelForm
from django.contrib.auth.models import Group

class UserGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['id', 'name']