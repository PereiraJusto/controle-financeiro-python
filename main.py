#==================================================
# Controle financeiro Pessoal
# Autor: Rafael Pereira
# Descrição: Programa em Python para registrar e acompanhar receitas, despesas, patrimonio e investimentos. Desenvolvido para aprendizado.
#Inicio do projeto: 16/10/2025
# Fim do projeto: 
#==================================================

from core.funcoes import adicionarRegistro, lerRegistros, caminhoReceita, caminhoDespesa, caminhoPatrimonio
import sys

def exibirMenu():
    print("\n=== Controle Financeiro ===")
    print("1. Regristrar Receita")
    print("2. Registrar Despesa")
    print("3. Registrar Patrimônio")
    print("4. Atualizar Aplicações e Investimentos")
    print("5. Gerar Relatórios Financeiros")
    print("6. Sair")

def main():
    while True:
        exibirMenu()
        opcao = input("Escolha uma opção (1-6): ")

        if opcao == "1":
            print("\n===REGISTRAR RECEITA===")
            mes = input("Mês/Ano (Ex: Out/2025): ")
            descricao = input("descição da receita: ")
            valor = input("Valor (R$): ")

            #Converte valor para float
            try:
                valor = float(valor.replace(',', '.'))
            except ValueError:
                print("Valor inválido!")
                continue

            dados ={
                "mes": mes,
                "descricao": descricao,
                "valor": valor
            }

            adicionarRegistro(caminhoReceita, dados, cabecalho=["mes", "descricao", "valor"])
            print("Receita registrada com sucesso!")
            
        elif opcao == "2":
            print("Função: registrar Despesa (em breve)")
        elif opcao == "3":
            print("Função: registrar Patrimônio (em breve)")
        elif opcao == "4":
            print("Função: atualizar Aplicações e Investimentos (em breve)")
        elif opcao == "5":
            print("Função: gerar Relatórios Financeiros (em breve)")
        elif opcao == "6":
            print("Saindo do programa...")
            sys.exit()
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()