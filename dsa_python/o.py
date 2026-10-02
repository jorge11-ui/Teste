print("ola")

points = {"MT1": 20, "MT2": 19, "MT3": 18, "Ins1": 8, "Ins2": 9}

num_curos = 0
total_pontos = 0
done = False
while not done:
    notas = input()

    if notas == "" or notas == " ":
        done = True

    elif notas not in points:
        print("nota nao-- {0} vai ser ignorada".format(notas))

    else:
        num_curos += 1 
        total_pontos += points[notas]

if num_curos > 0:
    print("A tua nota é {:.3f}".format(total_pontos / num_curos))
else:
    print("obg")
