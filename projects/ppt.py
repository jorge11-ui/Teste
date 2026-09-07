#Pedra papel tesoura
#As regras são:
    #tesoura ganha papel
    #papel ganha Pedra
    #Pedra ganha tesoura
    #E se forem iguais, é um empate

# função é randit() uma função construido num modulo "random", gera um numero inteiro aleatorio entre dois valores inteiros dados, os parametros são (inicio, fim)
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end = "")
#     print()
#
#
# import random
# n = random.randint(1, 10)
# print(n)



n=5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
print("\n")
n=5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

print("\n")
n=5
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print()
