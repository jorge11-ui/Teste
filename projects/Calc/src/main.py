from operations import (
    sum_basic,
    subtrair,
    multiplicacao,
    quadratic,
    divisao,
    sqrt,
    logarithm,
    factorial,
    exponent,
    div_inteira,
)

operacoes = {
    "1": ("Somar", sum_basic),
    "2": ("Subtrair", subtrair),
    "3": ("Multiplicar", multiplicacao),
    "4": ("Dividir", divisao),
    "5": ("Raiz quadrada", sqrt),
    "6": ("Equação quadrática", quadratic),
    "7": ("Logaritmo", logarithm),
    "8": ("Fatorial", factorial),
    "9": ("Expoente", exponent),
    "10": ("Divisão inteira", div_inteira),
}


def executar_terminal():
    while True:
        print("\n0 - Sair")
        for opcao, (nome, _) in operacoes.items():
            print(f"{opcao} - {nome}")

        escolha = input("Escolhe opção: ")
        if escolha == "0":
            print("Até à próxima!")
            break

        operacao = operacoes.get(escolha)
        if operacao is None:
            print("Opção inválida.")
            continue

        nome, funcao = operacao
        try:
            print(f"{nome}: {funcao()}")
        except ValueError:
            print("Entrada inválida. Introduz um número válido.")

        if input("\nPressiona Enter para continuar e 'N' para sair: ").upper() == "N":
            print("Programa encerrado")
            break

if __name__ == "__main__":
    executar_terminal()
