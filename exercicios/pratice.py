#filtrar apenas os numeros negativos

lista  = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos = [i for i in lista if i < 0]
print(negativos)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

numeros_achatados = [ numeros for rows in list_of_lists for numeros in rows]
print(numeros_achatados)

valor = input().split()
A = float(valor[0])
B = float(valor[1])
C = float(valor[2])
pi = 3.14159
retan_trian = (A * C) / 2
circle = pi * (C ** 2)
trapezio = ((A + B) * C) / 2
quadrado =  B ** 2
retangulo = B * A
print(f"TRIANGULO = {retan_trian:.3f}")
print(f"CIRCULO = {circle:.3f}")
print(f"TRAPEZIO = {trapezio:.3f}")
print(f"QUADRADO = {quadrado:.3f}")
print(f"RETANGULO = {retangulo:.3f}")
