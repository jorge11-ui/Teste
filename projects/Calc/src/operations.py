import cmath
import math


def formato(resultado, casas_decimais=3):
    """Arredonda valores numéricos sem alterar textos ou resultados complexos."""
    if isinstance(resultado, bool) or not isinstance(resultado, (int, float)):
        return resultado
    if isinstance(resultado, int) or not math.isfinite(resultado):
        return resultado

    resultado = round(resultado, casas_decimais)
    if resultado == 0:
        return 0
    if resultado.is_integer():
        return int(resultado)
    return resultado


def somar(a, b):
    return formato(a + b)


def subtrair_valores(a, b):
    return formato(a - b)


def multiplicar(a, b):
    return formato(a * b)


def dividir(a, b):
    if b == 0:
        return "Divisão sem solução: não é possível dividir por zero."
    return formato(a / b)


def raiz_quadrada(valor):
    if valor < 0:
        return "Raiz não real."
    return formato(math.sqrt(valor))


def resolver_quadratica(a, b, c):
    if a == 0:
        return "O coeficiente 'a' não pode ser zero."

    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        raiz = cmath.sqrt(discriminante)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        return f"x1 = {x1}\nx2 = {x2}"
    if discriminante == 0:
        x = -b / (2 * a)
        return f"x1 = x2 = {formato(x)}"

    raiz = math.sqrt(discriminante)
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    return f"x1 = {formato(x1)}\nx2 = {formato(x2)}"


def calcular_logaritmo(base, valor):
    if base <= 0 or base == 1:
        return "Erro: a base deve ser positiva e diferente de 1."
    if valor <= 0:
        return "Erro: o valor do logaritmando deve ser positivo."
    return formato(math.log(valor, base))


def calcular_fatorial(valor):
    if valor < 0 or not valor.is_integer():
        return "O fatorial só está definido para inteiros não negativos."
    return math.factorial(int(valor))


def calcular_potencia(base, expoente):
    try:
        return formato(math.pow(base, expoente))
    except (ValueError, OverflowError):
        return "Não foi possível calcular essa potência nos números reais."


def dividir_inteiros(a, b):
    if b == 0:
        return "Impossível dividir por zero."
    return formato(a // b)


# Wrappers para manter a interface de terminal existente.
def _ler_dois_numeros():
    return float(input("Número 1: ")), float(input("Número 2: "))


def sum_basic():
    return somar(*_ler_dois_numeros())


def subtrair():
    return subtrair_valores(*_ler_dois_numeros())


def multiplicacao():
    return multiplicar(*_ler_dois_numeros())


def divisao():
    return dividir(*_ler_dois_numeros())


def sqrt():
    return raiz_quadrada(float(input("Número: ")))


def quadratic():
    a = float(input("Escolhe o 'a': "))
    b = float(input("Escolhe o 'b': "))
    c = float(input("Escolhe o 'c': "))
    return resolver_quadratica(a, b, c)


def logarithm():
    base = float(input("Base: "))
    valor = float(input("Logaritmando: "))
    return calcular_logaritmo(base, valor)


def factorial():
    valor = float(input("Número: "))
    return calcular_fatorial(valor)


def exponent():
    base = float(input("Base: "))
    expoente = float(input("Expoente: "))
    return calcular_potencia(base, expoente)


def div_inteira():
    return dividir_inteiros(*_ler_dois_numeros())
