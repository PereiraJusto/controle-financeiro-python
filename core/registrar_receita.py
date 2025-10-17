#Função interativca para registrar receitas no CSV.

import os
from core.funcoes import adicionar_registro, caminho_receita

def registrar_receita_interativa():
    """
    Função que interafe com o usuário via terminal para registrar uma receita.
    Ela:
    - pede mês/ano, descrição, categoria e valor;
    - valida o valor numérico;
    - monta um dicionário com os campos; e
    - chama a função adicionarRegistro para persistir os dados no CSV.
    """

    print("\n=== Registrar Receita ===")
    mes = input("Mês/Ano (MM/AAAA): ").strip()
    descricao = input("Descrição da Receita: ").strip()
    categoria = input("Categoria (ex: ProLabore, Dividendos, Outros): ").strip()
    valor_raw = input("Valor da Receita: ").strip()

    try:
        if ',' in valor_raw and valor_raw.count(',') == 1 and '.' in valor_raw:
            valor_sanitizado = valor_raw.replace(',', '').replace(',', '.')
        else:
            valor_sanitizado = valor_raw.replace(',', '.')
        valor = float(valor_sanitizado)
    except ValueError:
        print("Valor inválido! Digite apenas números. Exemplo válido: 2800 ou 2800,00 ou 2.800,00")
        return
    
    dados = {
        "mes": mes,
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor
    }

    pasta_data = os.path.dirname(caminho_receita)
    if pasta_data and not os.path.exists(pasta_data):
        os.makedirs(pasta_data, exist_ok=True)

    adicionar_registro(caminho_receita, dados, cabecalho=["mes", "descricao", "categoria", "valor"])

    print("Receita registrada com sucesso!")
