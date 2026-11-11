import time
import os
from operations import sum_basic, subtrair, multiplicacao, quadratic, divisao, sqrt, logarithm


os.system('clear')
while True:
    print("\n0-Sair")
    print("1-Somar")
    print("2-Subtrair")
    print("3-Multiplicar")
    print("4-Dividir")
    print("5-Raiz quadrada")
    print("6-Quadratica")
    print("7-Logaritmo")
    escolha = input("Escolhe opcao: ")

    if escolha == "1":
        print("A soma é:", sum_basic())
    elif escolha == "2":
        print("A subtração é:", subtrair())
    elif escolha == "3":
        print("A multiplicação é:", multiplicacao())
    elif escolha == "4":
        print("A divisão é:", divisao())
    elif escolha == "5":
        print("A raiz quadrada é: ", sqrt())
    elif escolha == "6":
        print(quadratic())
    elif escolha == "7":
        print(logarithm())
    elif escolha == "0":
        print("Até à próxima!")
        break
    else:
        print("Opção inválida.")
    continuar = input("\nPressiona Enter para continuar e 'N' para sair: ").upper()
    if continuar == "N":
        print("Programa encerrado")
        break
    else:
        #waiting time
        start = time.time()
        print("\n...")
        time.sleep(1)
        end = time.time()
        print("")
