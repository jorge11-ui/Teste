# Funções

# O que aprender:
# - def / return
# - argumentos e parâmetros
# - escopo
# - argumentos por defeito / keyword args
# Escreve aqui os teus testes:
#

#Uma funcao pode ser definida usando o Keyword: def
#o objetivo de uma funcao é agrupar codigo que é executada varias vezes


#def nome_funcao(parametro): é um input que é definido para uma função
#argumento: é o valor do parametro
    #declaração

    #exprecao return

def fun():
    print("ola mundo")
fun() #--> chamar  a funcao para que ela seja executada func(), O codigo é executado quando a funcao é chamada
#Argumentos de funcoes
#def func(argumento) --> permitem funcoes receberem input data

def div_naodiv(x):
    if x % 2:
        return "divisivel"
    else:
        return "naodivisivel"

print(div_naodiv(16))
print(div_naodiv(3))

def diz_ola(nome):
    print("bom dia " + nome)
    print("boa tarde " + nome)
    print("boa noite " + nome)
diz_ola("jorge")

#retornar valores e retornar declarações
#ao criar uma função usando "def()" pode se especificar o valor do retorno com uma instrução de retorno:
    #o keyword return
    #o valor da funcao que se deve retornar

import random

def get_resposta(resposta_numero):
    if resposta_numero == 1:
        return "é certeza"
    elif resposta_numero == 2:
        return "Sem duvida"
    elif resposta_numero == 3:
        return "As perspectivas sao boas"
    elif resposta_numero == 4:
        return "Perguntava mais de novo mais tarde"
    elif resposta_numero == 5:
        return "Melhor nao dizer agora"
    elif resposta_numero == 6:
        return "Concentra te e pergunta mais uma vez"
    elif resposta_numero == 7:
        return "Nao contes com isso"
    elif resposta_numero == 8:
        return "A minha resposta é nao"
    elif resposta_numero == 9:
        return "as minhas fontes dizem que nao"


r = random.randint(1, 9)
print("escolhe um numero: ", r)
result = get_resposta(r)
print(result)


#none value- representa a ausencia de de um valor(tipo de dados: Nonetype)

import random

for i in range (100):
    if random.randint(0, 1) == 0:
        print("a", end=" ")
    else:
        print("b", end=" ")
print()

#Funcoes de dentro de funcoes: uma funcao definida dentro de outr funcao ºé chamad: nested function"
#É usada para organizar logica relacionada

def minha_funcao(x):
    x[0] = 20 #substitui o primeiro item por 20

b = [10, 20, 30]
minha_funcao(b)
print(b)


#Escopo - onde uma variavel é acessivel
#local: dentro da funcao
#global: fora da funcao

x = 100  # global

def mostra():
    x = 50  # local - so existe dentro da funcao
    print(x)

mostra()  # 50
print(x)  # 100


#Argumentos por defeito - valor pre definido caso nao seja enviado

def saudacao(nome="utilizador"):
    print("ola " + nome)

saudacao()       # ola utilizador
saudacao("jorge")  # ola jorge


#Keyword args - argumentos nomeados, nao precisam de ordem

def contactos(nome, telefone):
    print(nome + ": " + telefone)

contactos(telefone="912345678", nome="jorge")

def saudacoes():
    return "jorge"
def ano(nome):
    return f"17 {nome}"
print(ano(saudacoes()))


#Funcao lambda
#É uma funcao anonima pequena sem nome, ela pode receber qualquer tipo de argumento, mas so pode ter uma exprecao
#A funcao lambda nao usa return, mas retorna explicitamente a funcao
# x = lambda param1, param2, param3: param1 + param2 + param3
# print(x(arg1, arg2, arg3))

#exemplo funcao normal:
def somar_numeros(a, b):
    return a + b

print(somar_numeros(5, 5))

#ou em lambda
somar = lambda a, b: a + b
print(somar(5, 5))

#funcao lambda autoinvocada
print((lambda a, b: a + b)(5, 5))


# def gret_formatado(primeiro, ultimo, meio=""): # o meio nao pode vir antes dos outros argumentos, pq ele nao é um default argument
#     if meio:
#         nome_completo = primeiro + " " + meio + " " + ultimo
#     else:
#         nome_completo = primeiro + " " + ultimo
#     return nome_completo.title()
# musico = gret_formatado("Jorge", "tomas", "junior")
# print(musico)
#
#
# #uma funcao retornando um dicionario
#
# def pessoa_construir(membros, orgaos):
#     pessoa = {"Membros": membros, "Orgaos": orgaos} 
#     return pessoa
# fulano = pessoa_construir("maos", "coracao")
# print(fulano)
#
#
# def testewhile(primeiro_nome, ultimo_nome):
#     nome_completo = primeiro_nome + " " + ultimo_nome
#     return nome_completo.title()
#
# while True:
#     print("\nEnter your name")
#     print("Se quiseres sair press (q) e enter")
#     f_nome = input("primeiro nome: ")
#     if f_nome == "q":
#         break
#     l_nome = input("Ultimo nome: ") 
#     if l_nome == "q":
#         break
#     nome_formatado = testewhile(f_nome, l_nome)
#     print(f"\nOla {nome_formatado}")


design = ["iphone", "samsumg", "asus"]
modelos_completos = []

while design:
    autais = design.pop()
    
    print(f"Os modelos a fabricar: {autais.title()}")
    modelos_completos.append(autais)

print("\nModelos fabricados:")
for modelos_completo in modelos_completos:
     print(f"-{modelos_completo.title()}")

print("\n")
#dividir em duas funçoes:
def print_models(nao_printado, modelos_complets):
    while nao_printado:
        current_desing = nao_printado.pop()
        print(f"os Modelos a fabricar: {current_desing}")
        modelos_completos.append(current_desing)

def mostrar_modelos_completos(modelos_completos):
    print("\nModelos fabricados:")

    for model_complete in modelos_completos:
        print(model_complete.title())

nao_printado = ["iphone", "samsumg", "asus"]
modelos_completos = []

print_models(nao_printado[:], modelos_completos )
mostrar_modelos_completos(modelos_completos)


#Evitar que uma funcao modifique uma lista

#Para enviar uma copia da lista a funcao:
# nome_funcao(nome_lista[:]):
# [:]-- cria um copia da lista para ser enviada para a funcao
