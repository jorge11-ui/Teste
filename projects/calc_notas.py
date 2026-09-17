#gerador de recibo
import datetime as daste 
#cabecalho
print("============================================")
print("                 SUPERJORGE           ")
print("\n             Freeport outlet       ")
print("           Super mercado jorge          ")
print("=============================================")

print(("\nProdutos"))
lista = {
        "Chocolate": 2.99,
    "Manteiga": 3.99,
    "Farinha": 5.00
}
def adicionar_produto():
    for produto, preco in lista:
        print(produto, lista)
    adicionar = input("\nAdicione o produto: ")
    lista.append(adicionar)
    print("produto adicionado")
adicionar_produto()
adicionar_produto()
adicionar_produto()

print("\n----Produtos total-------")
print("\n".join([str(x) for  x in lista]))
print("A lista total dos produtos: ",len(lista))
