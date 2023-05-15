from django import forms
from . import models


class ContatoForm(forms.ModelForm):
    tipo = forms.CharField(
        label='Tipo',
        widget=forms.RadioSelect(choices=[('f', 'Fixo'), ('c', 'Celular')])
    )
    class Meta:
        model=models.Contato
        fields=('nome', 'sobrenome', 'fone', 'tipo')
