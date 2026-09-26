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
# {'marca': 'lamborghini', 'modelo': 'svj', 'ano': 2020}


#da para imprimir um item especifico do carro
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}
print(carro["modelo"])
# svj

#Acessar itens, é o mesmo metodo:
    #get()
x = carro.get("marca")
print(x)
# lamborghini
    #keys()- retorna com todas as chaves dentro do carronario
x =carro.keys()
print(x)
# dict_keys(['marca', 'modelo', 'ano'])

    #items- retorna cada item de uma lista como tuples dentro de uma lista
x =carro.items()
print(x)
# dict_items([('marca', 'lamborghini'), ('modelo', 'svj'), ('ano', 2020)])


#Mudar itens
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}

carro["modelo"] = "Urus"
print(carro)
# {'marca': 'lamborghini', 'modelo': 'Urus', 'ano': 2020}

#ou update()
carro.update({"modelo": "huracan"}) 
print(carro)
# {'marca': 'lamborghini', 'modelo': 'huracan', 'ano': 2020}

#Adicionar itens
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}
carro["ano"] = 2021
print(carro)
# {'marca': 'lamborghini', 'modelo': 'svj', 'ano': 2021}

#remover itens
  #pop()
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}
carro.pop("marca")
print(carro)
# {'modelo': 'svj', 'ano': 2020}

  #del
carro = {
    "marca": "lamborghini",
    "modelo": "svj",
    "ano": 2020
}

del carro ["ano"]
print(carro)
# {'marca': 'lamborghini', 'modelo': 'svj'}

#Nested dictionary usado para armanzenar um ou mais dicionarios dentro de um dicionario

alunos = {
    "aluno1": {
        "nome": "jorge",
        "idade": 17
    },
    "aluno2": {
        "nome": "joao",
        "idade": "18",
    }
}

#Para acessar esse dicionario
print(alunos)
print(alunos["aluno1"]["nome"])
# jorge
#para alterar:
alunos["aluno1"]["idade"] = 20
print(alunos["aluno1"])

#Para adicionar item
alunos["aluno1"]["curso"] = "Cs"

#Para percorrer todos os alunos
for aluno, dados in alunos.items():
    print(aluno)
    print("Nome:", dados["Nome"])
    print("Idade:", dados["idade"])