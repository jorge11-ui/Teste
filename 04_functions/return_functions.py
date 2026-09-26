#return serve para devolver um resultado de uma funcao

def somar_print(a, b):
    print(a + b)

resultado = somar_print(2, 5)
print(resultado)

#Com return

def somar(a, b):
    return a + b
resultado = somar(2, 4)
print(resultado)

#e pode ser usado denovo

#Quando um return é executado as linhas seguintes nao sao executados

def verificar(idade):
    if idade < 0:
        return "Idade invalida"

    if idade >= 18:
        return "Maior de idade"

    return "Menor de idade"

print(verificar(30))
print(verificar(13))
print(verificar(-20))

#substituir o else
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"

    return "ímpar"

#receber um argumento

def receber_argumento(nome):
    return f"ola {nome}".upper()

saudacao = receber_argumento("jorge")
print(saudacao)

#retornar varios valores

def varios_valores(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto

resultado = varios_valores(17, 5)
print(resultado)


def teste(a, b):
    mult = a * b
    div = a / b
    adicao = a + b
    sub = a - b
    return(
        f"Multiplicação: {mult}",
        f"Divisao: {div}", 
        f"Subtração: {sub}", 
        f"Adicao: {adicao}"
    )
num1 = float(input("Num1: "))
num2 = float(input("Num2: "))
result = teste(num1, num2)
for conta in result:
    print(conta)

