#Herença-quando uma classe herda da outra, ela automaticamente assumi todos os atributos e metodos da classe-pai

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


#nova classe

class CarroEletrico(Carro): #o nome da classe pai tem que ser incluido entre parenteses
    def __init_(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)

tesla = CarroEletrico("tesla", "X", "2021")
print(tesla.nome_descritivo())
