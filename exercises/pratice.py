#filtrar apenas os numeros negativos

lista  = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos = [i for i in lista if i < 0]
print(negativos)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

numeros_achatados = [ numeros for rows in list_of_lists for numeros in rows]
print(numeros_achatados)
