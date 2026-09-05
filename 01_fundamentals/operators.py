# #Operadores
#
# operadores aritmetricos:
#     +, -, *, /, %, //, **
#
# operadores de destribuição
#     x = 2
#     x += 2
#     x -= 3
#     x *= 3
#     x %= 4
#     x **= 3
#
# operador ternario
#  permite atribuir um valor se uma condicao for verdadeira e a outra falsa
#
num = 4

x = "é menor" if num < 10 else "nao é menor"
print(x)

x = "segunda" if num == 4 else "terça" if num == 5 else "quarta" if num == 6 else "sabado"
print(x)

#Operadoes logicos

x = 4
print(x > 10 or x > 3) #True

#Operadoes de identidade
#is - é True quando as duas variaveis sao iguais
#is not - é True quando as duas variaveis nao sao iguais
verduras = ["pepino", "tomate"]
frutas = ["pepino", "tomate"]
x = verduras

print(verduras is x)
print(frutas is verduras)
print(frutas == verduras)
print(verduras is not frutas)

#operadores de associação
#in
#not in
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("carne" not in  fruits)


#Operadores de Bit a bit (DEPOIS) porque envolve binarios
& - AND
|
^
~
<<
>>






