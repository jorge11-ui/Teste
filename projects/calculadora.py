#calculadora

num_1 = int(input("numero 1: "))
num_2 = int(input("numero 2: "))

print("Escolhe a sua operação")
print("1-Adição")
print("2-Subtração")
print("3-Multiplicação")
print("4-Divisão")

escolha =int(input("Escolhe a sua opção: "))


if escolha == 1:
    print(f"{num_1} + {num_2} = ", num_1 + num_2)
if escolha == 2:
    print(f"{num_1} - {num_2} = ", num_1 - num_2)
if escolha == 3: 
    print(f"{num_1} * {num_2} = ", num_1 * num_2)
if escolha == 4:
    print(f"{num_1} / {num_2} = ", num_1 / num_2)
