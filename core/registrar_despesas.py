# Função para registrar despesas de forma interativa
# Cria entradas automáticas apra despesas parcelas no cartão

import csv
from datetime import datetime
from core.utils import calcular_meses_futuros

def registrar_despesa_interativa():
    """Função principal para registrar despesas.
    Permite escolher forma de pagamento, parcelamente e salva no CSV.
    """

    caminhoDespesa = "data/despesas.csv"

    print("\n=== REGISTRAR DESPESA ===")

    mes = input("Mês/Ano (MM/AAAA): ").strip()
    descricao = input("Descrição da despesa: ").strip()
    valor = input("Valor (R$): ").strip()

    try:
        valor = float(valor.replace(",", "."))
    except ValueError:
        print("Valor inválido! Digite como 2800, 2800,00 ou 2.800,00")
        return
    
    formas_validas = {"1": "Dinheiro", "2": "Débito", "3": "Pix", "4": "Crédito"}
    forma_pagamento = ""
    while forma_pagamento not in formas_validas:
        print("Forma de pagamento: 1-Dinheiro, 2-Débito, 3-Pix, 4-Crédito: ")
        forma_pagamento = input("Escolha a forma de pagamento (1-4): ").strip()
        if forma_pagamento not in formas_validas:
            print("Opção inválida! Escolha entre as opções 1 a 4.")
    
    if forma_pagamento == "4":
        cartao = input("Nome do cartão: ").strip()
        parcelado = input("Despesa parcelada? (S/N): ").strip().upper()
        if parcelado == "S":
            try:
                total_parcelas = int(input("Quantidade de parcelas: ").strip())
                if total_parcelas < 1:
                    raise ValueError
            except ValueError:
                print("Número de parcelas inválido!")
                return
        else:
            total_parcelas = 1
    else:
        cartao = ""
        total_parcelas = 1
    
    try:
        mes_dt = datetime.strptime(mes, "%m/%Y")
    except ValueError:
        print ("Formato de mês inválido! Use MM/AAAA.")
        return
    
    meses_parcelas = calcular_meses_futuros(mes_dt, total_parcelas)

    valor_parcela = round(valor / total_parcelas, 2)

    with open(caminhoDespesa, mode="a", newline="", encoding="utf-8") as arquivo_csv:
        writer = csv.DictWriter(arquivo_csv, fieldnames=["mes", "descricao", "valor", "forma_pagamento", "cartao", "parcela_atual", "total_parcelas", "recorrente"])

        arquivo_csv.seek(0, 0)
        if arquivo_csv.tell() == 0:
            writer.writeheader()

        for i, mes_parcela in enumerate(meses_parcelas, start=1):
            registro ={
                "mes": mes_parcela,
                "descricao": descricao,
                "valor": valor_parcela,
                "forma_pagamento": forma_pagamento,
                "cartao": cartao,
                "parcela_atual": i,
                "total_parcelas": total_parcelas,
                "recorrente": "N"
            }
            writer.writerow(registro)

        
    print(f"Despesa registrada com sucesso! {total_parcelas} parcela(s) adicionada(s).")

