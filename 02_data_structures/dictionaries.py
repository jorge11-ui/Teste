# carronários

# O que aprender:
# - pares key / value
# - aceder, acarronar e remover
# - métodos (keys, values, items, get...)
# - iterar sobre carronários

#Os carronarios sao usados para armazenar valores, é uma coleção
#ordenada e modificavel e que nao permitem duplicados

#Sao escritos assim:


carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}
print(carro)


#da para imprimir um item especifico do carronario
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}
print(carro["modelo"])

#Acessar itens
    #get()
x = carro.get("marca")
print(x)
    #keys()- retorna com todas as chaves dentro do carronario
x =carro.keys()
print(x)

    #items- retorna cada item de uma lista como tuples dentro de uma lista
x =carro.items()
print(x)


#Mudar itens
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}

carro["modelo"] = "Urus"
print(carro)

#ou update()
carro.update({"modelo": "huracan"}) 
print(carro)

#Adicionar itens
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}
carro["ano"] = 2021
print(carro)

#remover itens
  #pop()
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}
carro.pop("marca")
print(carro)

  #del
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}

del carro ["ano"]
print(carro)


