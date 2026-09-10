
while True:
    print("=====Conversor de unidade_dists======")

    print("1-distancia")
    print("2-temperatura")
    print("3-Massa")
    print("4-Moeda")
    print("\n")
    converter = int(input("O que queres converter: "))
    print("Introduza a unidade_dist")
    #DISTANCIA


    if converter == 1:
        print("1.km-m")
        print("2.m-km")
        print("3.m-cm")

        unidade_dist = int(input("Qual a unidade(1-3): "))

        if unidade_dist < 1 or unidade_dist > 3:
            print("ErrorValue(nao incluido)")
        else:
            valor_distancia = float(input("valor a converter: "))

            if unidade_dist == 1:
                print(f"A distancia de {valor_distancia}km em metros é: {valor_distancia * 1000}m")
            elif unidade_dist == 2:
                print(f"A distancia de {valor_distancia}m em kilometros é: {valor_distancia / 1000}km")
            elif unidade_dist == 3:
                print(f"A distancia de {valor_distancia}m em centimetros é: {valor_distancia * 100}cm")

    elif converter == 2:
        print("1. De Celsius-Fahrenheit")
        print("2. De Fahrenheit-Celsius")
        unidade_temp = int(input("Qual é a unidade(1-2): "))

        if unidade_temp < 1 or unidade_temp > 2:
            print("ErrorValue(nao incluido)")
        else:
            valor_temp = float(input("valor a converter: "))

            if unidade_temp == 1:
                print(f"{valor_temp} ºC em Fahrenheit é: {(valor_temp * 1.8) + 32}F")
            elif unidade_temp == 2:
                print(f"{valor_temp} F em Celsius é: {((valor_temp - 32) / 1.8):.2f}ºC")
            else:
                print("ErrorValue")

    elif converter == 3:
        print("1.kg-g")
        print("2.g-kg")
        print("3.g-mg")
        unidade_massa =int(input("Qual é a unidade: "))
        if unidade_massa < 1 or unidade_massa > 3:
            print("ErrorValue(nao incluido)")
        else:
            valor_massa =float(input("valor a converter: "))

            if unidade_massa == 1:
                print(f"{valor_massa}kg em gramas é: {valor_massa * 1000} g")
            elif unidade_massa == 2:
                print(f"{valor_massa}g em kilogramas é: {valor_massa / 1000} kg")
            elif unidade_massa == 3:
                print(f"{valor_massa}g em miligramas é: {valor_massa * 1000} mg")
            else:
                print("ErrorValue")
    print("\n")
    escolha = input("Presse (sair) se quiser sair ou enter se quiser continuar: ")
    if escolha == "sair":
        break
    else:
        continue







