# Tratamento de Erros

# O que aprender:
# - try / except
# - else / finally
# - raise
# - exceções comuns

# Escreve aqui os teus testes:

#para saber se o nome foi fornecido com o nome do meio 

# def gret_formatado(primeiro, ultimo, meio=""): # o meio nao pode vir antes dos outros argumentos, pq ele nao é um default argument
#     if meio:
#         nome_completo = primeiro + " " + meio + " " + ultimo
#     else:
#         nome_completo = primeiro + " " + ultimo
#     return nome_completo.title()
# musico = gret_formatado("Jorge", "tomas", "junior")
# print(musico)
#
#
# #uma funcao retornando um dicionario
#
# def pessoa_construir(membros, orgaos):
#     pessoa = {"Membros": membros, "Orgaos": orgaos} 
#     return pessoa
# fulano = pessoa_construir("maos", "coracao")
# print(fulano)
#
#
# def testewhile(primeiro_nome, ultimo_nome):
#     nome_completo = primeiro_nome + " " + ultimo_nome
#     return nome_completo.title()
#
# while True:
#     print("\nEnter your name")
#     print("Se quiseres sair press (q) e enter")
#     f_nome = input("primeiro nome: ")
#     if f_nome == "q":
#         break
#     l_nome = input("Ultimo nome: ") 
#     if l_nome == "q":
#         break
#     nome_formatado = testewhile(f_nome, l_nome)
#     print(f"\nOla {nome_formatado}")

#
# design = ["iphone", "samsumg", "asus"]
# modelos_completos = []
#
# while design:
#     autais = design.pop()
#
#     print(f"Os modelos a fabricar: {autais.title()}")
#     modelos_completos.append(autais)
#
# print("\nModelos fabricados:")
# for modelos_completo in modelos_completos:
#      print(f"-{modelos_completo.title()}")
#
# print("\n")
# #dividir em duas funçoes:
# def print_models(nao_printado, modelos_complets):
#     while nao_printado:
#         current_desing = nao_printado.pop()
#         print(f"os Modelos a fabricar: {current_desing}")
#         modelos_completos.append(current_desing)
#
# def mostrar_modelos_completos(modelos_completos):
#     print("\nModelos fabricados:")
#
#     for model_complete in modelos_completos:
#         print(model_complete.title())
#
# nao_printado = ["iphone", "samsumg", "asus"]
# modelos_completos = []
#
# print_models(nao_printado[:], modelos_completos )
# mostrar_modelos_completos(modelos_completos)
#

#Evitar que uma funcao modifique uma lista

#Para enviar uma copia da lista a funcao:
# nome_funcao(nome_lista[:]):
# [:]-- cria um copia da lista para ser enviada para a funcao

