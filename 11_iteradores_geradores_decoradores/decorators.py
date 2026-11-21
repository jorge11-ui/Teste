# Decoradores

# O que aprender:
# - função dentro de função
# - @decorator básico
# - *args / **kwargs no wrapper
# - functools.wraps

# Escreve aqui os teus testes:
# Decoradores sao formas flexiveis para modificar ou extender comportamentos de funcoes



def mainfunc():
    print("ola mundo")
    def first_ins():
        print("jorge")
    def second_ins():
        print("junior")

    # a ordem de chamada das funcoes importa
    second_ins()
    first_ins()
mainfunc()

