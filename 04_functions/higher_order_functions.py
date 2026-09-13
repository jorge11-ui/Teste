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
