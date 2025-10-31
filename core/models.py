from django.db import models
from django.utils import timezone

class Lancamento(models.Model):
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]

    descricao = models.CharField(
        max_length=200,
        verbose_name='Descrição'
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Valor (R$)'
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        verbose_name='Tipo de Lançamento'
    )

    data = models.DateField(
        default=timezone.now,
        verbose_name='Data do Lançamento'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor} ({self.tipo})"
    
    class Meta:
        verbose_name = 'Lançamento'
        verbose_name_plural = 'Lançamentos'
        ordering = ['-data', '-criado_em']