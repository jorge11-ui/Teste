#Exercicios 

#Loops(for e while)

#1-print numero de 1 a 10
# numero = 1
# # while numero < 11:
# #     print(numero)
# #     numero += 1
# # print()
# #
# # #2-print numero de -10 a -1
# #count = 0
# number = 180
# while number > 10:
#     # divide number by 3
#     number = number / 3
#     # increase count
#     count = count + 1
# print('Total iteration required', count)
# # numero = -10
# while numero < 0:
#     print(numero)
#     numero = numero + 1  # -10 + 1= -9...
# print()




#Crie um programa que peça ao usuário que insira seu nome e sua idade. 
#Imprima uma mensagem dirigida a eles que lhes diz o ano em que completarão 100 anos de idade. 
#
# nome = "jorge"
# idade = 17
# daqui_100 = 2009 - 17 +100
# print("\n")
#

# n = 3
# if n % 2 != 0:
#     print("Weird")
# if 2 >= n <= 5:
#     print("Not Weird")
# if 6 <= n <= 20:
#     print("Weird")
# if n > 20:
#     print("Not Weird")
#
#
#
# for i in "jorgetomascusna":
#     if i == "a"  or i == "e":
#         break
#     print(i)
#
#
# frutas = ["maçã", "banana", "laranja"]
# for indice, fruta in enumerate(frutas):
#     print(f"índice {indice}: {fruta}")
#
# for i in range(1, 3):
#     for j in range(1,4):
#         print(i, j)


for i in range(2, 4):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j) 
print()
