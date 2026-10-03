# Organizador de PC - só com 01 a 08
# 01 variaveis/strings/input - 02 list/dict - 03 loops/if - 04 funcoes
# 05 import os/shutil - 06 try/except - 07 ficheiros txt - 08 classes

import os
import shutil


# 02: dicionario extensao -> pasta (igual ao que fizeste em conversor.py com TAXAS)
TIPOS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Musica": [".mp3", ".wav", ".ogg", ".flac"],
    "Documentos": [".pdf", ".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".md"],
    "Compactados": [".zip", ".rar", ".tar", ".gz"],
    "Codigo": [".py", ".js", ".html", ".css", ".json"]
}


class Organizador:
    # 08: classe simples como o teu Carro/Dog
    def __init__(self, pasta):
        self.pasta = pasta

    def pasta_destino(self, extensao):
        # 03 + 02: loop + dict
        for nome_pasta, extensoes in TIPOS.items():
            if extensao.lower() in extensoes:
                return nome_pasta
        return "Outros"

    def organizar(self):
        # 06: try/except como em errors.py
        try:
            ficheiros = os.listdir(self.pasta)
        except FileNotFoundError:
            print(f"Pasta nao encontrada: {self.pasta}")
            return
        except NotADirectoryError:
            print(f"Nao e uma pasta: {self.pasta}")
            return

        movidos = 0
        for nome in ficheiros:
            caminho_completo = os.path.join(self.pasta, nome)
            # 03: so ficheiros, ignora pastas
            if not os.path.isfile(caminho_completo):
                continue
            # ignora o proprio diario
            if nome == "diario.txt":
                continue

            _, ext = os.path.splitext(nome)
            destino_nome = self.pasta_destino(ext)
            destino_pasta = os.path.join(self.pasta, destino_nome)

            try:
                if not os.path.exists(destino_pasta):
                    os.makedirs(destino_pasta)
                shutil.move(caminho_completo, os.path.join(destino_pasta, nome))
                print(f"{nome} -> {destino_nome}/")
                movidos += 1
            except PermissionError:
                print(f"Sem permissao: {nome}")
            except Exception as e:
                print(f"Erro em {nome}: {e}")

        print(f"\nFeito! {movidos} ficheiro(s) organizados.")


# 04: funcoes pequenas como nas tuas calculadora.py / conversor.py
def renomear_em_lote():
    pasta = input("Pasta (ex: /home/jorge/Downloads): ").strip()
    prefixo = input("Prefixo novo (ex: foto_ferias): ").strip()

    if not prefixo:
        print("Prefixo vazio, a cancelar.")
        return

    try:
        ficheiros = sorted(os.listdir(pasta))
    except FileNotFoundError:
        print("Pasta nao encontrada.")
        return

    # 02 + 03: lista so de ficheiros
    so_ficheiros = []
    for f in ficheiros:
        if os.path.isfile(os.path.join(pasta, f)):
            so_ficheiros.append(f)

    if not so_ficheiros:
        print("Nada para renomear.")
        return

    print(f"\nVou renomear {len(so_ficheiros)} ficheiros. Exemplo:")
    for i, nome in enumerate(so_ficheiros[:3], start=1):
        _, ext = os.path.splitext(nome)
        print(f"  {nome} -> {prefixo}_{i}{ext}")

    confirma = input("Confirmar? (s/n): ").strip().lower()
    if confirma != "s":
        print("Cancelado.")
        return

    contador = 1
    for nome in so_ficheiros:
        _, ext = os.path.splitext(nome)
        novo_nome = f"{prefixo}_{contador}{ext}"
        try:
            os.rename(os.path.join(pasta, nome), os.path.join(pasta, novo_nome))
            print(f"{nome} -> {novo_nome}")
            contador += 1
        except Exception as e:
            print(f"Erro em {nome}: {e}")


def achar_grandes():
    # util para limpar o PC: acha ficheiros > X MB
    pasta = input("Pasta para analisar: ").strip()
    try:
        minimo = int(input("Tamanho minimo em MB [100]: ").strip() or "100")
    except ValueError:
        print("Numero invalido, a usar 100.")
        minimo = 100

    try:
        ficheiros = os.listdir(pasta)
    except FileNotFoundError:
        print("Pasta nao encontrada.")
        return

    # 02 + 04: lista de dicts como no teu Quiz
    grandes = []
    for nome in ficheiros:
        caminho = os.path.join(pasta, nome)
        if os.path.isfile(caminho):
            try:
                tamanho_mb = os.path.getsize(caminho) / (1024 * 1024)
                if tamanho_mb >= minimo:
                    grandes.append({"nome": nome, "mb": round(tamanho_mb, 1)})
            except OSError:
                continue

    if not grandes:
        print(f"Nenhum ficheiro >= {minimo} MB.")
        return

    # ordenar do maior para o menor (sort simples, sem precisar de 16_dsa)
    for i in range(len(grandes)):
        for j in range(i + 1, len(grandes)):
            if grandes[j]["mb"] > grandes[i]["mb"]:
                grandes[i], grandes[j] = grandes[j], grandes[i]

    print(f"\nFicheiros grandes (>= {minimo} MB):")
    for g in grandes:
        print(f"  {g['mb']} MB - {g['nome']}")


def diario():
    # 07: with open como em files.py / teste.txt
    while True:
        print("\n--- Diario ---")
        print("[1] Escrever")
        print("[2] Ler")
        print("[3] Voltar")
        op = input("Escolha: ").strip()

        if op == "1":
            texto = input("Escreve: ").strip()
            if texto:
                try:
                    with open("diario.txt", "a", encoding="utf-8") as f:
                        f.write(texto + "\n")
                    print("Guardado em diario.txt")
                except OSError as e:
                    print(f"Erro a guardar: {e}")
        elif op == "2":
            try:
                with open("diario.txt", "r", encoding="utf-8") as f:
                    conteudo = f.read()
                if conteudo.strip():
                    print("\n" + conteudo)
                else:
                    print("Diario vazio.")
            except FileNotFoundError:
                print("Ainda nao tens diario.txt")
        elif op == "3":
            break
        else:
            print("Opcao invalida.")


def mostrar_menu():
    print("\n===== ORGANIZADOR DE PC =====")
    print("[1] Organizar pasta por tipo")
    print("[2] Renomear ficheiros em lote")
    print("[3] Achar ficheiros grandes")
    print("[4] Diario rapido")
    print("[5] Sair")


def main():
    # mesmo padrao while que usaste na calculadora.py
    while True:
        mostrar_menu()
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            pasta = input("Pasta (ex: /home/jorge/Downloads): ").strip()
            org = Organizador(pasta)
            org.organizar()
        elif escolha == "2":
            renomear_em_lote()
        elif escolha == "3":
            achar_grandes()
        elif escolha == "4":
            diario()
        elif escolha == "5":
            print("Ate logo!")
            break
        else:
            print("Escolha invalida.")
        input("\nPrime Enter para continuar...")


if __name__ == "__main__":
    main()
