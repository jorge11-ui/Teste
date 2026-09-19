from decimal import Decimal

while True:
    print("=====Conversor de unidade======")

    print("1-distancia")
    print("2-temperatura")
    print("3-Massa")
    print("4-Moeda")
    print("5-Area")
    print("\n")
    converter = int(input("O que queres converter: "))
    print("Introduza a unidade")
    #DISTANCIA


    if converter == 1:
        print("====Voce escolheu Distancia=====")
        distancia_listas = ["1.Km-m", "2.m-Km", "3.m-cm"]
        for distancia_lista in distancia_listas:
            print(distancia_lista)

        unidade_dist = int(input("Qual a unidade(1-3): "))

        if unidade_dist < 1 or unidade_dist > 3:
            print("ErrorValue(nao incluido)")
        else:
            valor_distancia = float(input("valor a converter: "))
 
            if unidade_dist == 1:
                print(f"A distancia de {valor_distancia}km em metros sao: {valor_distancia * 1000}m")
            elif unidade_dist == 2:
                print(f"A distancia de {valor_distancia}m em kilometros sao: {valor_distancia / 1000}km")
            elif unidade_dist == 3:
                print(f"A distancia de {valor_distancia}m em centimetros sao: {valor_distancia * 100}cm")

    elif converter == 2:
        print("====Voce escolheu Temperatura=======")
        temperatura_listas = ["1. De Celsius-Fahreinheit", "2.De Fahreinheit-Celsius"]
        for temperatura_lista in temperatura_listas:
            print(temperatura_lista)
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
        print("======Voce escolheu Massa======")
        massa_listas = ["1.Kg-g", "2.g-kg", "3.g-mg"]
        for massa_lista in massa_listas:
            print(massa_lista)
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

    elif converter == 4:
        TAXAS = {
            'EUR': Decimal('1.0000'),
            'USD': Decimal('1.0925'),
            'BRL': Decimal('5.4530'),
            'GBP': Decimal('0.8560')
        }
        print("====Voce escolheu Moeda========")
        print("As moedas disponiveis para a conversão")
        print("As conversoes disponiveis sao:",list(TAXAS.keys()))

        valor = Decimal(input("Introduza o valor:"))
        origem = input("Origem: ").upper().strip()
        destino = input("Destino: ").upper().strip()

        if origem and destino == TAXAS:   
             valor_euro = valor/TAXAS[origem]
             valor_resultado = valor_euro * TAXAS[destino] 
             resultado_final = valor_resultado.quantize(Decimal())
             print(f"Resultado: {resultado_final} {destino}")

        else:
            print("Input ErrorValue")

    elif converter == 5:

        def area_converter(valor, unidade_area):
            if unidade_area == 1: #km para  m
                return valor * 1000000
            elif unidade_area == 2: #Hm para m
                return valor * 10000
            else:
                return  None  

        print("Escolhe a conversao:")
        distacina_areas = ["1.Km2 para m2", "2.Hm2 para m2"]
        for distacina_area in distacina_areas:
            print(distacina_area)
        opcao_escolhida = int(input("Escolhe a conversão(1 ou 2): "))
        valor_area = float(input("Valor da area: "))
        resultado = area_converter(valor_area, opcao_escolhida)
        
        if resultado is not None:
            print(f"O resultado é: {resultado}")
        else:
            print("Error")

        ####################

    print("\n")
    escolha = input("Presse (sair) se quiser sair ou enter se quiser continuar: ")
    if escolha == "sair":
        break
    else:
         continue
