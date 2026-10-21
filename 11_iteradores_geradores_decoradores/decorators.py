# Decoradores
# O que aprender:
# - função dentro de função
# - @decorator básico
# - *args / **kwargs no wrapper
# - functools.wraps

# Decoradores sao formas flexiveis para modificar ou extender comportamentos de funcoes
#
def decorador(func):
    def wrapper():
        print("Antes de chamar a funcao")
        func()
    return wrapper
@decorador
def greet():
    print("Ola mundo ")
greet()
# é basicamente uma funcao que que usa outra funcao como argumento

def decor(func):
    def wrapper():
        print("Antes")
        func()
        print("Depois")
    return wrapper
@decor #pega a funcao jj como um argumento
def jj():
    print("Ola")
jj()

#decoradores com parametros
def decorator(func):
    def wrapper():
        print(f"ola mundo antes {func.__name__}")
        func()
        print("completo")
    return wrapper()

@decorator
def minha_func():
    print("minha funcao")

@decorator
def outra_func():
    print("outra funcao")

#ou
def myfunction(func):
    def winner():
        return func().upper()
    return winner #retornar so o nome da vuncao nao a funcao(winner())

@myfunction
def otrofuncao():
    return "Ola jorge"
print(otrofuncao())

#*args e **kwargs
def changecase(func):
  def mywinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return mywinner

@changecase
def minha_function(nam):
  return "Hello " + nam

print(minha_function("JJ"))
