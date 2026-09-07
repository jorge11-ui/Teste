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
#def nome_funcao(parametro):

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

