# Loops

# O que aprender:
# - for loop
# - while loop
# - break / continue
# - range()


#pode se fazer um bloco de codigo repitir se muitas vezes com while, a condição da instrução é verdadeira

#Uma instrução while consiste em:
#1-a palavra while
#2-uma condição(True ou False)
#3-colon

#as isntrucoes if e while sao semelhantes, mas se executar por exemplo
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
#     #o break serve para interroper 
#


coun = 0
while coun < 5:
    print(coun)
    coun += 1
else:
    print(coun)


