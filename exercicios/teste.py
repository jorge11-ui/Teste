#Exercicios 

#Loops(for e while)

#1-print numero de 1 a 10
numero = 1
# while numero < 11:
#     print(numero)
#     numero += 1
# print()
#
# #2-print numero de -10 a -1
#
# numero = -10
# while numero < 0:
#     print(numero)
#     numero = numero + 1  # -10 + 1= -9...
# print()




#Crie um programa que peça ao usuário que insira seu nome e sua idade. 
#Imprima uma mensagem dirigida a eles que lhes diz o ano em que completarão 100 anos de idade. 

nome = str(input("por favor escreva o seu nome: "))
idade = int(input("por favor escreva a sua idade: "))

daqui_100 = 2009 - idade + 100
print(nome +", Voce tera 100 anos em : " + str(daqui_100))


