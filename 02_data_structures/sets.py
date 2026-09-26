# Sets

# O que aprender:
# - criar sets
# - adicionar / remover
# - operações (união, interseção, diferença)

# Escreve aqui os teus testes:

#Sets sao coleções de valores unicos e sem ordem garantida
#pode ser criados strings, integers, float

#exemplo:
frutas = {"maça", "banana", "laranja"}
print(frutas)


#para criar um set vazio
vazio = set() #{} cria um dicionario vazio numa set

#add e remove
frutas = {"maça", "banana", "laranja"}
frutas.add("morango")
print(frutas)


#remove(dá erro se o item nao existir), pode usar-se discard
frutas = {"maça", "banana", "laranja"}
frutas.remove("banana")
frutas.discard("abacate")
print(frutas)

#clear para limpar tudo
frutas = {"maça", "banana", "laranja"}
frutas.clear()
print(frutas)


#operações entre sets

set1 = {1, 2, 3, 4, 5, 6}
set2 = {6, 7, 8, 3, 9}
print(set1 | set2) #uniao entre os elementos unicos das sets

print(set1 & set2) #interseção de elementos presentes nos dois sets 

print(set1 - set2) # diferença- elementos que estao presentes em set1 mas nao em set2

print(set1 ^ set2) #diferença simetrica- elementos que estao apenas em um dos sets


#Verificar elementos

carros = {"bmw", "mercediz", "ferrari", "toyota"}

print("ferrari" in carros) #True
print("tesla" in carros) #False

#Remover items duplicados de uma lista
carros = ["bmw", "mercediz", "ferrari", "toyota", "bmw", "ferrari"]

carros_unicos = set(carros) 
print(carros_unicos)

carros_unicos = list(set(carros)) #retornar uma lista( a ordem original pode ser perdida)