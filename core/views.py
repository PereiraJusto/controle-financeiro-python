from django.shortcuts import render
from .models import Lancamento
from decimal import Decimal

def lista_lancamentos(request):
    """
    View que exibe uma lista de todos os lançamentos financeiros
    """
    lancamentos = Lancamento.objects.all().order_by('-data', '-criado_em')

    total_receitas = sum(Decimal(str(l.valor)) for l in lancamentos if l.tipo == 'receita')
    total_despesas = sum(Decimal(str(l.valor)) for l in lancamentos if l.tipo == 'despesa')
    saldo = total_receitas - total_despesas

    context = {
        'lancamentos': lancamentos,
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo,
    }

    return render(request, 'core/lista_lancamentos.html', context)

def nova_despesa(request):
    return render(request, 'core/nova_despesa.html')

def nova_receita(request):
    return render(request, 'core/nova_receita.html')
