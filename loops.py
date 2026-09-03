# Loops

# O que aprender:
# - for loop
# - while loop
# - break / continue
# - range()

#quando usar loops:
    #para autommatizar e repetir tarefas
    #interação indefenida
    #reduzir a complexidade
    #loop infinito

#pode-se fazer um bloco de código repetir-se muitas vezes com while, enquanto a condição da instrução for verdadeira

#Uma instrução while consiste em:
#1-a palavra while
#2-uma condição(True ou False)
#3-colon

#as instruções if e while são semelhantes, mas se executar por exemplo
#
# x = 0
# if x < 3:
#     print("vezes")
# #while é usada para executar um bloco de codigo repetidamente ate que ela seja satisfeita enquanto verdadeira
# y = 0
# while y < 3:
#     print("vezes")
#     y = y + 1 # o y = y + numero - serve para alterar o valor do y a cada repetição
#
# name =""
# while name != "Jorge":
#     print("pfv nome")
#     name = input(">")
# print("obg,", name)
#
# fome = 5
#
# while fome > 0:
#     print(f"nao estou satisfeito: falta {fome} comida")
#     fome -= 1
# print("hahaha finalmente estou satisfeito")
#
# # #break
#     #o break serve para interromper 
#


# coun = 0
# while coun < 5:
#     print(coun)
#     coun += 1
# else:
#     print(coun)

#1. para imprimir os primeiros 10 numeros naturais
numero = 1
while numero < 11:
    print(numero)
    numero += 1
print()




# ============ FOR LOOP ============
#
# O for loop percorre os elementos de uma sequência (lista, string, range, etc.)

# Sintaxe básica:
# for variavel in sequencia:
#     bloco de código

# # Exemplo com lista
# frutas = ["maçã", "banana", "laranja"]
# for fruta in frutas:
#     print(fruta)
#
# # Exemplo com string
# letras = "python"
# for letra in letras:
#     print(letra)
#
# # ============ RANGE() ============
# # range() gera uma sequência de números
# # range(stop) → vai de 0 até stop-1
# # range(start, stop) → vai de start até stop-1
# # range(start, stop, step) → vai de start até stop-1 com passo
#
# # Imprime 0 a 4
# for i in range(5):
#     print(i)
#
# # Imprime 2 a 6
# for i in range(2, 7):
#     print(i)
#
# # Imprime 0, 2, 4, 6, 8 (de 2 em 2)
# for i in range(0, 10, 2):
#     print(i)
#
# # Imprime 10, 9, 8, 7, 6 (contagem regressiva com step negativo)
# for i in range(10, 5, -1):
#     print(i)
#
# ============ BREAK ============
# O break interrompe o loop imediatamente quando é executado

# Exemplo: para no número 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# Saída: 1 2 3 4

# # Exemplo com while
counter = 0
while True:  # loop infinito
    counter += 1
    if counter == 3:
        break
    print(counter)
# Saída: 1 2
#
# # ============ CONTINUE ============
# # O continue pula a iteração atual e vai para a próxima
#
# # Exemplo: imprime apenas os pares
# for i in range(1, 11):
#     if i % 2 != 0:  # se for ímpar, pula
#         continue
#     print(i)
# # Saída: 2 4 6 8 10
#
# # Exemplo: pula o número 3
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
# # Saída: 1 2 4 5
#
# # ============ WHILE...ELSE ============
# # O bloco else de um while é executado quando a condição se torna falsa
# # (não é executado se o loop for interrompido com break)
#
# num = 0
# while num < 3:
#     print(num)
#     num += 1
# else:
#     print("loop terminou normalmente")
# # Saída: 0 1 2 "loop terminou normalmente"
#
# # ============ FOR...ELSE ============
# # Mesmo conceito: o else é executado se o loop terminar sem break
#
# for i in range(5):
#     if i == 10:  # nunca vai ser verdade, então o else executa
#         break
# else:
#     print("nenhum break foi executado")
#
# # ============ LOOP COM ENUMERATE() ============
# # enumerate() retorna o índice e o valor de cada elemento
#
# frutas = ["maçã", "banana", "laranja"]
# for indice, fruta in enumerate(frutas):
#     print(f"índice {indice}: {fruta}")
#
# # Pode definir o índice inicial
# for indice, fruta in enumerate(frutas, start=1):
#     print(f"{indice}º: {fruta}")
#
# # ============ LOOP COM ZIP() ============
# # zip() combina dois ou mais iteráveis elemento por elemento
#
# nomes = ["Ana", "Bia", "Carlos"]
# notas = [9, 7, 10]
# for nome, nota in zip(nomes, notas):
#     print(f"{nome} tirou {nota}")
#
# # ============ LOOP COM DICIONÁRIO ============
# pessoa = {"nome": "Jorge", "idade": 25, "cidade": "Porto"}
#
# # percorrer as chaves
# for chave in pessoa:
#     print(chave)
#
# # percorrer chaves e valores com .items()
# for chave, valor in pessoa.items():
#     print(f"{chave}: {valor}")
#
# # ============ LOOP ANINHADO ============
# # Um loop dentro de outro
#
# # Tabuada de multiplicar
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i} x {j} = {i*j}")
#     print()  # linha em branco entre cada tabuada
#
# # ============ COMPREENSÃO DE LISTAS (LIST COMPREHENSION) ============
# # Forma reduzida de criar listas com loops
#
# # Forma normal
# quadrados = []
# for x in range(1, 6):
#     quadrados.append(x ** 2)
#
# # Com list comprehension (mesmo resultado, mais compacto)
# quadrados = [x ** 2 for x in range(1, 6)]
#
# # Com condição
# pares = [x for x in range(1, 11) if x % 2 == 0]
