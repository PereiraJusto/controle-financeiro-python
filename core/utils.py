# Funções auxiliares para o projeto de controle financeiro

from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcular_meses_futuros(mes_inicial, total_parcelas):
    """
    Recebe:
    - mes_inicial: datetime do primeiro mês
    - total_parcelas: int, número total de parcelas
    Retorna:
    - lista de strings "MM/AAAA" correspondentes a cadas parcela
    """

    meses = []
    for i in range(total_parcelas):
        mes_atual = mes_inicial + relativedelta(months=i)
        meses.append(mes_atual.strftime("%m/%Y"))
    return meses