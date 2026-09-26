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