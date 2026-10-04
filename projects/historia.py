import os


compras =  []
dinheiro = []


class Sacola():
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco


        try:
            nome = str(input(""))
            quantidade = int(("input"))
            preco = float(("input"))

        except:
            print("Voce introduziu alguma coisa errada")

mostrar = Sacola

print(mostrar)

