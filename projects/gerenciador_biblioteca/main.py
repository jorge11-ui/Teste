# Dados iniciais
livros = [
    {
        "Nome": "Pensamentos",
        "Autor": "Marco Aurelio",
        "Categoria": "Filosofia",
        "Ano": 180,
        "Disponibilidade": "Sim"
    },
    {
        "Nome": "Ola",
        "Autor": "Marco Aurelio",
        "Categoria": "Filosofia",
        "Ano": 2023,
        "Disponibilidade": "Não"
    }
]

# Menu Principal
def menu_principal():
    print("\n" + "=" * 50)
    texto_gb = "Gestor De Biblioteca"
    print(texto_gb.center(50))
    print("=" * 50)
    print("[1] Pesquisar Livros")
    print("[2] Lista de todos os livros")
    print("[3] Adicionar livros")
    print("[4] Emprestar livros")
    print("[5] Sair")
    print("=" * 50)

# Função para listar todos os livros em formato de tabela

def pesquisar_livros():
    buscar_item = input("Introduza o livro que gostaria de pequisar: ").lower()
    livros_encotrados = []
   
    if not buscar_item:
        print("\nLivro nao encontrado")

    else:
        for livro in livros:
            if buscar_item in livro["Nome"].lower() or buscar_item in livro["Autor"].lower() or buscar_item in livro["Categoria"].lower() or buscar_item in str(livro["Ano"]):
                livros_encotrados.append(livro)
        
        if livros_encotrados:
            print("Resultados encotrados")
            for livro in livros_encotrados:
                print(f"\nLivro {livro["Nome"]}, {livro["Autor"]}")

        else:
            print("Livro nao encotrado")


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

listar_livros()


def adicionar_livros():
    pass
adicionar_livros()

def emprestar_livros():
    pass
emprestar_livros()



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
        emprestar_livros()
    elif escolher_opcao == 5:
        print("Obrigado pela visita, ate logo")
        break
    else:
        print("Escolhe uma opcao valida")
