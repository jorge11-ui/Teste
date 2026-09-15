import random

aleatorio = random.randint(1, 50)

print("Ola, advinha o numero secreto")

while True:
  escolha = int(input("Escolha um numero de 1 a 50: "))
  if escolha < aleatorio:
    print("Advinha mais alto")

  elif escolha > aleatorio:
    print("Advinha mais baixo")
    
  elif escolha == aleatorio:
    print("Voce ganhou!!")
    break
  else:
    print("Fora da opcao ou opcao invalida")