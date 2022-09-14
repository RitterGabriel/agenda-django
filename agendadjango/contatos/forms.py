from django import forms
from .models import *

class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','sobrenome','telefone','email',
                  'data_nascimento','descricao','categoria']