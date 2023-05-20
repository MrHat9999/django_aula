from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from . import models


def validar_fone(value):
    if value and len(value) != 9:
        raise ValidationError(str(value) + " não é um número de telefone válido, deve ter 8 dígitos!")


class ContatoForm(forms.ModelForm):
    tipo = forms.CharField(
        label="Tipo",
        widget=forms.RadioSelect(choices=[("f", "Fixo"), ("c", "Celular")]),
    )
    nome = forms.CharField(label="Nome", validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(60)])
    fone = forms.CharField(validators=[validar_fone])

    class Meta:
        model = models.Contato
        fields = ("nome", "sobrenome", "fone", "tipo")
