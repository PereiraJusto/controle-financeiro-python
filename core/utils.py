# Funções auxiliares para o projeto de controle financeiro

from datetime import datetime

def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def add_months(dt, months):
    """
    Adiciona um número de meses a um datetime, preservando o dia quando possível.
    """
    month = dt.month - 1 + months
    year = dt.year + month // 12
    month = month % 12 + 1
    # dias por mês, considerando ano bissexto para fevereiro
    days_in_month = [31, 29 if _is_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = min(dt.day, days_in_month[month - 1])
    return datetime(year, month, day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)

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
        mes_atual = add_months(mes_inicial, i)
        meses.append(mes_atual.strftime("%m/%Y"))
    return meses