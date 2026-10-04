# Decoradores

# O que aprender:
# - função dentro de função
# - @decorator básico
# - *args / **kwargs no wrapper
# - functools.wraps

# Escreve aqui os teus testes:
# Decoradores sao formas flexiveis para modificar ou extender comportamentos de funcoes
#
def decorator(func):
    def wrapper():
        print("Antes de chamar a funcao")
        func()
    return wrapper
@decorator
def greet():
    print("Ola mundo ")
greet()
