# Ficheiros (Input e Output)

# O que aprender:
# - open / close
# - ler e escrever
# - with statement
# - ficheiros de texto

# Escreve aqui os teus testes:

#Guardar dados permanentes, mesmo quando o programa fecha
#Acessar files externos(csv, txt, json)

#para abrir um file é usado o open() - file = open("file.txt", "mode")

file = open("teste.txt", "r" )
#para fechar file


#files properties
print("Filename", file.name)
print("Mode", file.mode)
print("Esta fechado?", file.closed) #True ou False
#Ler um file
#Escrever um file
# with open("teste.txt", "w") as file: #w abri o file para(writing)
#     escrever = input("Escreve alguma coisa: ")
#     file.write(escrever)
# print("escrito.")
#
#para ler um file
with open("teste.txt", "r") as file:
    ler_file = file.read()
print(ler_file)


