from random import choice

opcoes = ["pedra", "papel", "tesoura"]
primeira_vez = True
while primeira_vez:
    if primeira_vez:
        print("Vamos jogar!!!!!")
    else:
        print("Queres jogar outra vez?? ")
    play = input("\n(s/n): ").lower()
    if play == "s" or "sim":
        escolha_computador = choice(opcoes)
        primeira_vez = False
        for opcao in opcoes:
            print(opcao.upper())
        escolha_user = input("Escolha uma opcao valida: ").lower()

        if escolha_user not in opcoes:
            print("Opcao invalida")
            continue
        elif escolha_user == escolha_computador:
            print(f"Voce escolheu: {escolha_user}")
            print(f"O computador escolheu: {escolha_computador}")
            print("Empatado")

        #Onde o user sempre ganha
        elif (escolha_user in  "papel" and escolha_computador == "pedra") or \
            (escolha_user == "pedra" and escolha_computador == "tesoura") or \
            (escolha_user == "tesoura" and escolha_computador == "papel"):
            print(f"Voce escolheu: {escolha_user}")
            print(f"O computador escolheu: {escolha_computador}")
            print("Voce ganhou")
        elif (escolha_computador == "papel" and escolha_user == "pedra") or \
            (escolha_computador == "pedra" and escolha_user == "tesoura") or \
            (escolha_computador == "tesoura" and escolha_user == "papel"):
            print(f"Voce escolheu: {escolha_user}")
            print(f"O computador escolheu: {escolha_computador}")
            print("Voce perdeu")

    elif play == "n" or "nao":
        print("Ok, tchau")
        primeira_vez = False
    else:
        print("Opcao invalida, tente outra vez")
        continue
