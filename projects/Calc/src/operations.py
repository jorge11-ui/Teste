import math
import time
import cmath

def formato(resultado):
    if resultado.is_integer():
        return int(resultado)
    return resultado

def sum_basic():
    number1 =float(input("Numero 1: "))
    number2 =float(input("Numero 2: "))
    return formato(number1 + number2)

def subtrair():
    number1 = float(input("Numero 1: "))
    number2 = float(input("Numero 2: "))
    return formato(number1 - number2)

def multiplicacao():
    number1 = float(input("Numero 1: "))
    number2 = float(input("Numero 2: "))
    return formato(number1 * number2)


def divisao():
    number1 = float(input("Numero 1: "))
    number2 = float(input("Numero 2: "))
    if number2 == 0:
        return "Divisao sem solucao"
    return formato(number1 / number2)

def sqrt():
    number1 = float(input("Numero 1: "))
    if number1 < 0:
        return "Raiz nao real"
    return formato(math.sqrt(number1))

def quadratic():
    try:
        a = int(  input("\nEscolhe o 'a': "))
        if a == 0:
            print("'a' não pode ser 0 ")
            return
        b = float(input("Escolhe o 'b': "))
        c = float(input("Escolhe o 'c': "))
    except ValueError:
        return "Error: Introduz uma opcao valida(apenas numeros)."

    disc = (b ** 2) - (4 * a * c)

    if disc < 0:
        x1 = (-b + cmath.sqrt(disc))
        x2 = (-b - cmath.sqrt(disc))
        print("A equacao possui duas raizes complexas")
        return f"x1 = {x1} \nx2 = {x2}"
    elif disc == 0:
        x = -b / (2*a)
        return f"x1 = x2 = {x:.2f}"
    else:
        x1 = (-b + cmath.sqrt(disc)) / 2*a
        x2 = (-b - cmath.sqrt(disc)) / 2*a
        print("A equacao possui duas raízes reais distintas")
        return f"x1 = {x1:.2f} ou x2 = {x2:.2f}"
def logarithm():
    try:
        base = int(input("base: "))
        de = int(input("De: "))
        if base <= 0 or base == 1:
            return "Erro: a base deve ser maior do que 0 ou 1"
        if de <= 0:
            return "Erro: O valor (De) deve ser maior do que 0"

        resultado = math.log(de, base)
        return f"O Logaritmo é {resultado:.4f}"
    except ValueError:
        return "Error"
