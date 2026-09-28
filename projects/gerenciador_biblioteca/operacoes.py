from livro import livros


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
            f"Status: {livro['Status']}"
        )


def listar_livros():
    linha = "-" * 106
    print("\n" + linha)
    # Cabeçalho
    print(
        f"{'Nome':<22} | {'Autor':<20} | {'Categoria':<14} | "
        f"{'Ano':<6} | {'Status':<12} | {'Disp':<6}"
    )
    print(linha)

    for livro in livros:
        # Imprime os VALORES do dicionário livro
        print(
            f"{livro['Nome']:<22} | {livro['Autor']:<20} | "
            f"{livro['Categoria']:<14} | {livro['Ano']:<6} | "
            f"{livro['Status']:<12} | {livro['Disponibilidade']:<6}"
        )
    print(linha)


def ler_ano(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Ano inválido, escreve um número (ex: 1532 ou -375)")


def adicionar_livros():
    print("\nAdicionar livro")
    print("=" * 50)

    nome = input("Nome do livro: ").strip()
    autor = input("Autor: ").strip()

    if not nome or not autor:
        print("O nome e o autor são obrigatórios")
        return False

    categoria = input("Categoria: ").strip() or "Sem categoria"
    ano = ler_ano("Ano: ")
    status = input("Status (Quero ler / A ler / Lido): ").strip() or "Quero ler"

    novo_livro = {
        "Nome": nome,
        "Autor": autor,
        "Categoria": categoria,
        "Ano": ano,
        "Status": status,
        "Disponibilidade": "Sim",
    }
    livros.append(novo_livro)
    print(f"\nLivro adicionado: {nome}")
    return True

