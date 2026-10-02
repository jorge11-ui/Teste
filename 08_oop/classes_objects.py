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

class Dog: #definir uma classe chamado Cao
    especie = "Pastor alemao"
    def __init__(self, name, age):
        self.name = name #usa o valor armazenado no parametro name e o armazena na variavel name
        self.age = age

    def sentar(self): #self refere ao objeto atual e é usado para armazer dados dentro dele
        print(self.name.title() + "agora esta a sentar")

cao1 = Dog("Romeu", 3)
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

class Ca(Animal):
    def ladrar(self):
        print(f"{self.nome} esta a ladrar")

#Chamar metodos- para chamar uma funcao é preciso especificar a instancia e o metodo separados por um ponto
c = Ca("Jj")
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


class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.distancia_percorrida = 0


    def nome_descritivo(self):
        nome_completo = self.marca +  ", " + self.modelo + ", " + str(self.ano)
        return nome_completo.title()
    
    def ler_hodometro(self):
        print(f"Esse carro tem {str(self.distancia_percorrida)} km percorridos")

    def update_car_distance(self, kilometragem):
        self.distancia_percorrida = kilometragem

carro_novo = Carro("audi", "a4", 2016)
print(carro_novo.nome_descritivo())
carro_novo.ler_hodometro()

#Modificar o valor de um atributo
carro_novo.distancia_percorrida = 20
carro_novo.ler_hodometro()

#Modificar o valor de atributo com um metodo
carro_novo.update_car_distance(23)
carro_novo.ler_hodometro()



