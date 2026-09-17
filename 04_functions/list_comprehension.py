# List Comprehension

# O que aprender:
# - list comprehension
# - dict comprehension
# - comprehension com condição
# - comprehension aninhada

# Escreve aqui os teus testes:
#
#

#Transformar um string em lista 
string = "Jorge"
lista = list(string)
print(lista)


squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

#Uma list Comprehension permite gerar listas em apenas uma linha de codigo

squares = [value**2 for value in range(1, 11)]

print(squares)


aliens = []

for numero_aliens in range(1, 30):
    novo_alien = {"cor": "verde", "altura": "2 metros"}
    aliens.append(novo_alien)


for alien in aliens[0: 3]:
    if alien["cor"] is "verde":
        alien["cor"] = "amarelo"
        alien["altura"] = "3 metros"

for alien in aliens[0: 10]:
    print(alien)


