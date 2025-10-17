#==================================================
# Controle financeiro Pessoal
# Autor: Rafael Pereira
# Descrição: Programa em Python para registrar e acompanhar receitas, despesas, patrimonio e investimentos. Desenvolvido para aprendizado.
#Inicio do projeto: 16/10/2025
# Fim do projeto: 
#==================================================

from core.funcoes import adicionar_registro, ler_registros, caminho_receita, caminho_despesa, caminho_patrimonio
from core.registrar_receita import registrar_receita_interativa
from core.registrar_despesas import registrar_despesa_interativa
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
           registrar_receita_interativa()            
        elif opcao == "2":
            registrar_despesa_interativa()
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