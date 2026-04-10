from django.db import models
from datetime import date

class Demanda(models.Model):
    TIPOS = [
        ("Projeto", "Projeto"),
        ("Vistoria", "Vistoria"),
        ("Postar", "Postar"),
        ("Voltar assinado", "Voltar assinado"),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    voltar_assinado = models.BooleanField(default=False)
    data_criacao = models.DateField(default=date.today)
    posicao = models.PositiveIntegerField(default=0)

    @property
    def dias_de_criacao(self):
        return (date.today() - self.data_criacao).days

    @property
    def cor_status(self):
        dias = self.dias_de_criacao
        if dias <= 1:
            return "verde"
        elif dias <= 3:
            return "amarelo"
        else:
            return "vermelho"

    def __str__(self):
        return self.titulo