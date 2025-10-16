import csv
import os

#Caminhos para os arquivos CSV
caminhoReceita = os.path.join("data", "receitas.csv")
caminhoDespesa = os.path.join("data", "despesas.csv")
caminhoPatrimonio = os.path.join("data", "patrimonios.csv")

#Função genérica para adicionar registro em CSV
def adicionarRegistro(caminhoArquivo, dados, cabecalho):
    arquivoExiste = os.path.isfile(caminhoArquivo)

    with open(caminhoArquivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=cabecalho)

        #Escreve o cabeçalho se o arquivo não existir
        if not arquivoExiste:
            write.writeheader()

        #Escreve os dados
        writer.writerow(dados)

#função para ler todos os registros de um CSV
def lerRegistros(caminhoArquivo):
    if not os.path.isfile(caminhoArquivo):
        return []
    
    with open(caminhoArquivo, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)