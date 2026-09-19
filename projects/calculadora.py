# ATM
from decimal import Decimal
import re

saldo = Decimal("0.00")
historico = []

def mostrar_menu():
    print("============Menu================")
    print("\n1.Depositar dinheiro")
    print("2.Consultar saldo")
    print("3.Levantar dinheiro")
    print("4.Transferir dinheiro")
    print("5.Historico")
    print("6.Sair")

def depositar():
    global saldo
    quantidade = Decimal(input("Valor a depositar: "))
    saldo += quantidade
    historico.append(quantidade)
    print(f"\nVoce depositou: {quantidade:.2f} 💵")
    print(f"Voce tem {saldo} 💵 na sua conta")

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
    destinatario = str(input("Destinatario(nome): "))

    if not destinatario.replace(" ", " ").isalpha():
        print("Erro: O nome deve conter apenas letras")
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
    entrada = input("Escolha: ")

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
    elif escolha == 6:

        print("A sair do ATM, ate logo!")
        return False
    else:
        print("Escolha invalida tente novamente ou saia")
    return True


#loop
continuar = True
while continuar:
    mostrar_menu()
    continuar = opcoes()
    if continuar:
        input("Press enter")
        print("\n" * 2)
    
