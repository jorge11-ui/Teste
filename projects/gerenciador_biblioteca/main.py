from time import sleep
from livro import livros
from gestor import gestor_emprestimo
from operacoes import adicionar_livros, listar_livros, pesquisar_livros

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


def main():
    while True:
        menu_principal()
        try:
            escolher_opcao = int(input("Escolhe uma opção: "))
        except ValueError:
            print("Escolhe uma opcao valida")
            continue

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


if __name__ == "__main__":
    main()
