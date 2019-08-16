from django.forms import ModelForm
from .models import PessoaModel,CboModel


class CboForms(ModelForm):
    class Meta:
        model = CboModel
        fields =  ['nome_cbo'] 