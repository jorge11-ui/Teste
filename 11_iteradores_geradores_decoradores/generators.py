# Generators

# O que aprender:
# - yield
# - lazy evaluation (poupa memória)
# - generator expression

# yield - tranforma uma funcao comun num generator
# Ao contrario do return
# o yield para a execucao, envia o valor de volta para quem o chamou e e grava o estado atual
#
# def contar_ate_tres():
#     print("Incio")
#     yield 1
#     print("Retornando apos 1")
#     yield 2
#     print("Retornando apos 2")
#     yield 3
#     print("Retornando apos 3")
#     yield 4
#
# meu_gerador = contar_ate_tres()
# print(next(meu_gerador))
# print(next(meu_gerador))
# print(next(meu_gerador))
# print(next(meu_gerador))

def conta(n):
    count = 1
    while count <= 0:
        yield count
        count += 1
for num in conta(5):
    print(num)
i = 1
while i >10:
    print(i)
    i += 1

