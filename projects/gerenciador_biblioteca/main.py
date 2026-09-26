# Dados iniciais
from datetime import datetime
from time import sleep

from livro import livros
emprestimos = []

# Menu Principal
def menu_principal():
    print("\n" + "=" * 50)
    texto_gb = "Gestor De Biblioteca"
    print(texto_gb.center(50))
    print("=" * 50)
    print("[1] Pesquisar Livros")
    print("[2] Lista de todos os livros")
    print("[3] Adicionar livros")
    print("[4] Opcoes emprestimo")
    print("[5] Sair")
    print("=" * 50)



def pesquisar_livros():
    buscar_item = input("Introduza o livro que gostaria de pesquisar: ").strip().lower()
    livros_encontrados = []

    for livro in livros:
        if (
            buscar_item in livro["Nome"].lower()
            or buscar_item in livro["Autor"].lower()
            or buscar_item in livro["Categoria"].lower()
            or buscar_item in str(livro["Ano"])
        ):
            livros_encontrados.append(livro)

    if not livros_encontrados:
        print("\nLivro não encontrado")
        return

    print("\nResultados encontrados")
    for livro in livros_encontrados:
        print(
            f"\nLivro: {livro['Nome']} | Autor: {livro['Autor']} | "
            f"Disponibilidade: {livro['Disponibilidade']}"
        )


def listar_livros():
        linha_traço = "-" * 90
        print("\n" + linha_traço)
        # Cabeçalho
        print(f"{'Nome':<22} | {'Autor':<20} | {'Categoria':<12} | {'Ano':<10} | {'Disp':<10}")
        print(linha_traço)

        for livro in livros:
            # Imprime os VALORES do dicionário livro
            print(f"{livro['Nome']:<22} | {livro['Autor']:<20} | {livro['Categoria']:<12} | {livro['Ano']:<10} | {livro['Disponibilidade']:<10}")
        print(linha_traço)



def adicionar_livros():
    pass


def gestor_emprestimo():
    while True:
        print("\n" + "=" * 50)
        print("Gestor de emprestimos de livros")
        print("\n" + "=" * 50)
        print("[1]Registar novo emprestimo")
        print("[2]Registar devolução")
        print("[3]Ver historico de emprestimos")
        print("[4]Sair")
        print("=" * 50)

        try:
            pesquisar_emprestimo = int(input("Escolha um opção: "))
        except ValueError:
            print("Escolha uma opção válida")
            continue

        if pesquisar_emprestimo == 1:
            emprestimo_livro()
        elif pesquisar_emprestimo == 2:
            registar_devolucao()
        elif pesquisar_emprestimo == 3:
            historico_emprestimos()
        elif pesquisar_emprestimo == 4:
            break
        else:
            print("Escolha uma opção válida")



def ler_data(mensagem):
    while True:
        data_texto = input(mensagem).strip()

        try:
            return datetime.strptime(data_texto, "%d-%m-%y").strftime("%d-%m-%y")
        except ValueError:
            print("Data inválida, escreve no formato (DD-MM-YY)")


def emprestimo_livro():
    nome_leitor = input("Nome do leitor: ").strip()
    nome_livro = input("Nome do livro: ").strip()

    if not nome_leitor or not nome_livro:
        print("Por favor preencha esses campos")
        return

    livro_encontrado = None
    for livro in livros:
        if livro["Nome"].casefold() == nome_livro.casefold():
            livro_encontrado = livro
            break

    if livro_encontrado is None:
        print("Livro não encontrado")
        return

    if livro_encontrado["Disponibilidade"] == "Não":
        print("Este livro já está emprestado")
        return

    data_emprestimo = ler_data("Data de emprestimo(DD-MM-YY): ")
    livro_encontrado["Disponibilidade"] = "Não"
    emprestimos.append({
        "leitor": nome_leitor,
        "livro": livro_encontrado["Nome"],
        "data_emprestimo": data_emprestimo,
        "data_devolucao": None
    })

    sleep(1.5)
    print(f"Empréstimo registado: {nome_livro.upper()}")
    sleep(2)


def registar_devolucao():
    emprestimos_ativos = [
        emprestimo for emprestimo in emprestimos
        if emprestimo["data_devolucao"] is None
    ]

    if not emprestimos_ativos:
        print("Não existem empréstimos ativos")
        return

    for emprestimo in emprestimos_ativos:
        print(f"{emprestimo['livro']} - {emprestimo['leitor']}")

    nome_livro = input("Nome do livro a devolver: ").strip()
    emprestimo_encontrado = None

    for emprestimo in emprestimos_ativos:
        if emprestimo["livro"].casefold() == nome_livro.casefold():
            emprestimo_encontrado = emprestimo
            break

    if emprestimo_encontrado is None:
        print("Empréstimo ativo não encontrado")
        return

    data_devolucao = ler_data("Data de devolução(DD-MM-YY): ")
    emprestimo_encontrado["data_devolucao"] = data_devolucao

    for livro in livros:
        if livro["Nome"].casefold() == nome_livro.casefold():
            livro["Disponibilidade"] = "Sim"
            break

    print(f"Devolução registada: {nome_livro}")


def historico_emprestimos():
    if not emprestimos:
        print("Ainda não existem empréstimos registados")
        return

    for emprestimo in emprestimos:
        estado = "Emprestado" if emprestimo["data_devolucao"] is None else "Devolvido"
        data_devolucao = emprestimo["data_devolucao"] or "Sem devolução"
        print(
            f"Livro: {emprestimo['livro']} | Leitor: {emprestimo['leitor']} | "
            f"Empréstimo: {emprestimo['data_emprestimo']} | "
            f"Devolução: {data_devolucao} | Estado: {estado}"
        )




while True:
    menu_principal()
    escolher_opcao = int(input("Escolhe uma opção: "))

    if escolher_opcao == 1:
        pesquisar_livros()
    elif escolher_opcao == 2:
        listar_livros()
    elif escolher_opcao == 3:
        adicionar_livros()
    elif escolher_opcao == 4:
        gestor_emprestimo()
    elif escolher_opcao == 5:
        print("Obrigado pela visita, ate logo")
        break
    else:
        print("Escolhe uma opcao valida")

    sleep(2)
