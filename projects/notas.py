#Verificador de notas

print("---------Verificador de notas------------")
print("As notas sao de 0, 20")
print("\n")

notas = float(input("Coloques a sua notas: "))

if notas < 9.5:
    print("negativa")

elif notas < 13.5:
  print("Suficiente")

elif notas < 16.5:
  print("Bom")

elif notas < 17.5:
  print("Muito Bom")

elif notas <= 20:
  print("Excelente")

else:
    print("erro, nota invalida")

