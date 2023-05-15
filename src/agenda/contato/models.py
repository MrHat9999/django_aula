from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    fone = models.IntegerField(verbose_name="telefone")
    tipo = models.CharField(choices=(("c", "Celular"), ("f", "Fixo")), max_length=1)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, null=True)

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
