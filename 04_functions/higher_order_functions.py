# Funções de Ordem Superior

# O que aprender:
# - lambda
# - map / filter / reduce
# - sorted com key

#Uma  HOF é uma funcao que trabalha com outras funcoes, pode aceitar uma funcao como argumento, retornar uma funcao ou fazer os dois
def nome(func):
    return func("jorge")
def upper(text):
   return text.upper() 

print(nome(upper))
#nome aceita upper como um argumento
#upper pega na string é transforma em Maiusculas

def func_apply(func, x):
    return func(x)

def square(n):
    return n * n

print(func_apply(square, 5))
# 25


# Lambda: funcao pequena e sem nome, com apenas uma expressao
dobrar = lambda numero: numero * 2
print(dobrar(4))
# 8

# map: aplica uma funcao a cada elemento
numeros = [1, 2, 3, 4]
quadrados = map(square, numeros)
print(list(quadrados))
# [1, 4, 9, 16]

# Tambem podemos usar lambda com map
dobrados = map(lambda numero: numero * 2, numeros)
print(list(dobrados))
# [2, 4, 6, 8]

# filter: mantem os elementos para os quais a funcao devolve True
pares = filter(lambda numero: numero % 2 == 0, numeros)
print(list(pares))
# [2, 4]

# reduce: combina os elementos e acumula um resultado
from functools import reduce

soma = reduce(lambda total, numero: total + numero, numeros)
print(soma)
# 10

# Para uma soma simples, sum() costuma ser mais claro
print(sum(numeros))
# 10

# sorted com key: a funcao em key define como comparar os elementos
nomes = ["jorge", "Ana", "miguel"]
nomes_ordenados = sorted(nomes, key=str.lower)
print(nomes_ordenados)
# ['Ana', 'jorge', 'miguel']

alunos = [
    {"nome": "Ana", "idade": 17},
    {"nome": "Jorge", "idade": 20},
    {"nome": "Miguel", "idade": 16},
]
alunos_por_idade = sorted(alunos, key=lambda aluno: aluno["idade"])
print(alunos_por_idade)
# [{'nome': 'Miguel', 'idade': 16}, {'nome': 'Ana', 'idade': 17}, {'nome': 'Jorge', 'idade': 20}]

# Uma funcao tambem pode devolver outra funcao
def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator

    return multiplicar


dobrar_numero = criar_multiplicador(2)
print(dobrar_numero(5))
# 10
