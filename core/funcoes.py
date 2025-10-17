import csv
import os

#Caminhos para os arquivos CSV
caminho_receita = os.path.join("data", "receitas.csv")
caminho_despesa = os.path.join("data", "despesas.csv")
caminho_patrimonio = os.path.join("data", "patrimonios.csv")

#Função genérica para adicionar registro em CSV
def adicionar_registro(caminho_arquivo, dados, cabecalho):
    arquivo_existe = os.path.isfile(caminho_arquivo)

    with open(caminho_arquivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=cabecalho)

        #Escreve o cabeçalho se o arquivo não existir
        if not arquivo_existe:
            write.writeheader()

        #Escreve os dados
        writer.writerow(dados)

#função para ler todos os registros de um CSV
def ler_registros(caminho_arquivo):
    if not os.path.isfile(caminho_arquivo):
        return []
    
    with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)