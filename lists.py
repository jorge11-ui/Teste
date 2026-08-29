# Listas

# O que aprender:
# - criar listas
# - indexação / slicing
# - métodos (append, remove, sort...)
# - iterar sobre listas

# Escreve aqui os teus testes:

paises = ["Portugal", "França", "Espanha", "Guine-bissau",'Denmark','Finland','Norway','Iceland']
pt, fr, es, gb, *scan = paises
print(pt)
print(fr)
print(es)
print(gb)
print(scan)

#Remover itens de listas
lst = ["item1", "item2"]
lst.remove("item1")
print(lst) #so remove o primeiro item da lista(item1)

