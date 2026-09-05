# Listas

# O que aprender:
# - criar listas
# - indexação / slicing
# - métodos (append, remove, sort...)
# - iterar sobre listas

lista = ["jorge", "junior", "coisa"]
print(lista)

#uma lista pode conter qualquer tipo de "data"
lista2 = [True, False, True, False]
lista3 = [1, 2, 3, 4, 5]

# posit =  ["jorge", "junior", "coisa"]
#             0         1         2
# negat =  ["jorge", "junior", "coisa"]
#            -3        -2          -1
#
#itens de acesso

paises = ["Portugal", "França", "Espanha", "Guine-bissau",'Denmark','Finland','Norway','Iceland']
print(paises[5:]) #nao inclui Finland

#para verificar se um item esta numa lista
paises = ["Portugal", "França", "Espanha", "Guine-bissau",'Denmark','Finland','Norway','Iceland']
if "Portugal" in paises:
    print("portugal esta na lista")


#alterar um item 
paises = ["Portugal", "França", "Espanha", "Guine-bissau",'Denmark','Finland','Norway','Iceland']
paises[2] = "Alemanha" #substitui Espanha por Alemanha
print(paises)
#adicionar itens a lista
paises = ["Portugal", "França", "Espanha", "Guine-bissau",'Denmark','Finland','Norway','Iceland']
paises.append("Brasil")
print(paises)

#inserir em uma determinada posição
paises = ["Portugal", "França", "Espanha", "Guine-bissau",'Denmark','Finland','Norway','Iceland']
paises.insert(3, "Mexico")

#ampliar um lista adicionando outra
paises = ["Portugal", "França", "Espanha", "Guine-bissau",'Denmark','Finland','Norway','Iceland']
america = ["Mexico", "Chile"]
paises.extend(america) # Ou extend()--> pode ser adicionado qualquer objeto
print(paises)
----------------------//--------------------------------//------------------------------//----------------------------

paises = ["Portugal", "França", "Espanha", "Guine-bissau",'Denmark','Finland','Norway','Iceland']
pt, fr, es, gb, *scan = paises
print(pt)
print(fr)
print(es)
print(gb)
print(scan)

#Remover itens de listas
lst = ["item1", "item2"]
lst.remove("item1") #remove o item especificado e se houver mais de um item com o mesmo valor, so remove o primeiro item
print(lst)

#Remover indice(1, 2, 3, etc)
frutas = ["banana", "maça", "morango"]
frutas.pop(1) # se e nao for especificado nenhum item(pop()), removerá o ultimo item
print(frutas)

#Mesma coisa com del
frutas = ["banana", "maça", "morango"]
del frutas[1]
print(frutas)

#del tambem pode remover a lista toda
frutas = ["banana", "maça", "morango"]
del frutas

#clear(), esvazia a lista, mas ainda continua a existir
frutas = ["banana", "maça", "morango"]
frutas.clear()
print(frutas)



