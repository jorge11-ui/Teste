from decimal import Decimal
import re

saldo = Decimal("0.00")
historico = []

def mostrar_menu():
    # Cores ANSI
    AZUL = "\033[1;34m"
    VERDE = "\033[1;32m"
    VERMELHO = "\033[1;31m"
    RESET = "\033[0m"

    print(f"{AZUL}┌────────────────────────────────────┐{RESET}")
    print(f"{AZUL}│         🏦 SISTEMA BANCÁRIO        │{RESET}")
    print(f"{AZUL}├────────────────────────────────────┤{RESET}")
    print("│  [1] 💵  Depositar                 │")
    print("│  [2] 💳  Consultar Saldo           │")
    print("│  [3] 🏧  Levantar Dinheiro         │")
    print("│  [4] 💸  Transferir                │")
    print("│  [5] 📜  Histórico                 │")
    print(f"│  {VERMELHO}[6] 🚪  Sair                      {RESET}│")
    print(f"{AZUL}└────────────────────────────────────┘{RESET}")

def depositar():
    global saldo
    quantidade = Decimal(input("Valor a depositar: "))
    saldo += quantidade
    historico.append(quantidade)
    print(f"\nVoce depositou: {quantidade:.1f} 💵")
    print(f"Voce tem {saldo:.1f} 💵 na sua conta")

def consultar():
    print(f"\nSaldo atual é: {saldo} 💵")

def levantar():
    global saldo
    valor_levantar = Decimal(input("Valor a levantar: "))

    if valor_levantar > saldo:
        print("\nValor insuficiente")
    else:
        saldo -= valor_levantar
        historico.append(f"Levantamento de -{valor_levantar} 💵 ")

        print(f"Voce levantou {valor_levantar} 💵")
        print(f"O seu saldo atual é {saldo} 💵")

def transferir():

    global saldo
    destinatario = str(input("Destinatario(nome): ")).strip()

    if not destinatario.replace(" ", " ").isalpha():
        print("Erro: O nome deve conter apenas letras")
        return
    else:
        print(f"\nNome valido: {destinatario}")

    valor_transferir = Decimal(input("Valor a transferir: "))

    if valor_transferir > saldo:
        print("\nValor insuficiente")
    else:
        saldo -= valor_transferir
        historico.append(f"Transferencia para {destinatario} de {valor_transferir} 💵")
        print(f"\nTransferido {valor_transferir} 💵 para {destinatario} com sucesso")
        print(f"Saldo atual de {saldo}💵")

def ver_historicos():
    print("=============Historico=============")

    if not historico:
        print("Sem operacoes feitas")
    else:
        for i in historico:
            print(i)

def opcoes():
    AZUL = "\033[1;34m"
    VERDE = "\033[1;32m"
    VERMELHO = "\033[1;31m"
    RESET = "\033[0m"
    entrada = input(f"\n{VERDE}👉 Escolha uma opção: {RESET}")

    if entrada == "":
        return True
    try:
        escolha = int(entrada)
    except ValueError:
        print("Por favor introduza uma opcao valida")
        return True

    if escolha == 1:
        depositar()
    elif escolha == 2:
        consultar()
    elif escolha == 3:
        levantar()
    elif escolha == 4:
        transferir()
    elif escolha == 5:
        ver_historicos()
    elif escolha == 6 or "sair":
        print("Obrigado por utilizar os nossos serviços")
        return False
    else:
        print("Tente novamente")
    return True
#loop
continuar = True
while continuar:
    mostrar_menu()
    continuar = opcoes()
    if continuar:
        input("Press enter para continuar ou ´sair´: ")
        if "sair" or "sai":
            break
        print("\n" * 2)

