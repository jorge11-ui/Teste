# Tratamento de Erros

# O que aprender:
# Tipos de erros
# - try / except
# - else / finally
# - raise
# - exceções comuns

# Escreve aqui os teus testes:


#Exemplos de excecoes comuns

# ValueError: valor invalido para a conversao
try:
    int("abc")
except ValueError:
    print("ValueError")

# TypeError: tipos incompatíveis numa operacao
try:
    "3" + 2
except TypeError:
    print("TypeError")

# ZeroDivisionError: divisao por zero
try:
    10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")

# KeyError: chave inexistente num dicionario
try:
    pessoa = {"nome": "Jorge"}
    pessoa["idade"]
except KeyError:
    print("KeyError")

#usar try para indicar codigo que pode falhar e except para tratar uma execeção especifica
while True:
    try:
        numero = int(input("Escreve um numero: "))
        print(10 / numero)
        break
    except ValueError:
        print("Escreve um numero inteiro")
        continue

    except ZeroDivisionError:
        print("Nao podes dividir zero")
        continue
    finally:
        print("Obrigado, ate logo") #finally- o finally executa no fim tendo o codigo sido executado ou nao 
    