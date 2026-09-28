# Classes e Objetos

# O que aprender:
# - class / __init__ / self
# - métodos e atributos
# - herança

# Escreve aqui os teus testes:
#

#criando um Classe
"""
criando uma classe em python
class NomeClasse(objeto):
    ------------------
"""

class Cao: #definir uma classe chamado Cao
    especie = "Pastor alemao"
    def __init__(self, name, age):
        self.name = name #usa o valor armazenado no parametro name e o armazena na variavel name
        self.age = age

    def sentar(self): #self refere ao objeto atual e é usado para armazer dados dentro dele
        print(self.name.title() + "agora esta a sentar")

cao1 = Cao("Romeu", 3)
print(cao1.name)
print(cao1.age)

"""
Metodo __init__, é um metodo que executa automaticamente sempre que criamos um novo pedido 
baseado na classe Cao
O parametro self é obrigatorio na definicao do metodo e deve estar antes dos outros parametros
Qualquer variavel prefixado com self esta disponivel a todos os metodos da classe
"""

"""
Metodo __ str__()
"""
#Herança- uma classe pode receber caracteristicas da outra

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som generico ")

class Cao(Animal):
    def ladrar(self):
        print(f"{self.nome} esta a ladrar")

c = Cao("Jj")
c.falar()
c.ladrar()


#Encapsulamento(__something)
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo #privado

    def mostrar_saldo(self):
        return self.__saldo

#Polimorismo-objetos diferentes podem responder ao mesmo metodo(som)
class Gato:
    def som(self):
        return "Miauuuu"

class Cao:
    def som(self):
        return "AU au au au au"