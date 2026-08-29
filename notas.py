# variaveis e tipos
# As variaveis nao podem começam com numeros,
# nao podem ter espaço
#
# as variveis podem ser escritas:
#    nome 
#    valor_total
#    pais11
#    _numeros
#    skills = {
#
# }
# Tipos de variaveis    
#    string #Ex: nomes, paises... tudo o que estiver em ""
#    integer # numeros inteiros
#    float # numeros decimais
#    bool # True ou False
#    complex # operações complexas
#    list # []
# Exemplos:
num_int = 10.99

print(int(num_int))

num_float = 10.30
print(float(num_float))


         # Operadores
# Adição
# Subtração
# Multiplicação
# Divisão
# Modulo %
# Divisao inteira //
# Exponenciação **
#

#operadores de comparação
# == ->igual
# != ->diferente
# <
# >
# <=
# >=

##Operadores logicos
#and -- true se os ambos as declarações forem verdadeiras
#or  -- true se uma das declarações forem verdadeiras
#not -- true se nenhuma das declarações forem verdadeiras

#Strings
# \ --> quebra linha
# \t --> adiciona 4 espaços(tab)
# print(".......\".oal\"...")

#list- é a forma de guardar varios valores dentro
# de uma variavel
# Ex: frutas = [maça, pera, uva, banana]
#                0     1     2     3
# Podes guardar diferentes tipos de dados
# list = ["jorge", 10, 2.22, True]
# print(list[0]) ----> jorge
#
# frutas = ["maça", "morango", "banana"]
# frutas[1] = "uva"
# print(frutas)
#

nota = 75

if nota >= 90:
    print("A")
elif nota >= 70:
    print("B")
elif nota >= 50:
    print("C")
else:
    print("F")


nome = ""
if nome:          # equivalente a: if nome != ""
    print("Tem nome")
else:
    print("Nome vazio")   # <-- executa


