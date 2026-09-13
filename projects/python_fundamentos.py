# =============================================================
# PYTHON FUNDAMENTOS - Tutorial com exemplos práticos
# =============================================================
# Cada secção ensia um conceito que falta no math.py
# Executa com: python python_fundamentos.py
# =============================================================


# ──────────────────────────────────────────────
# 1. FUNÇÕES
# ──────────────────────────────────────────────
# Funções guardam código reutilizável.
# Em vez de repetir o mesmo código 4 vezes,
# escreves uma vez e chamas sempre que precisas.

def saudar(nome):
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}!"


def somar(a, b):
    """Soma dois números."""
    return a + b


# Função com valor por omissão (default)
def potencia(base, expoente=2):
    """Eleva uma base a um expoente. Por defeito: ao quadrado."""
    return base ** expoente


# Chamar as funções
print("=== 1. FUNÇÕES ===")
print(saudar("Jorge"))              # Olá, Jorge!
print(somar(3, 5))                  # 8
print(potencia(4))                  # 16 (usa default=2)
print(potencia(2, 10))             # 1024
print()


# ──────────────────────────────────────────────
# 2. TRATAMENTO DE ERROS (try / except)
# ──────────────────────────────────────────────
# Se o utilizador digitar "abc" quando se pede um número,
# o Python crasha com ValueError.
# O try/except apanha esse erro e mostra uma mensagem amigável.

print("=== 2. TRY / EXCEPT ===")

# SEM tratamento (vai crashar se input não for número):
# numero = int(input("Digite um número: "))  # ← ValueError!

# COM tratamento:
try:
    # Ist o aqui tenta executar o código
    numero = int("42")
    print(f"Conversão ok: {numero}")
except ValueError:
    # Só executa se houver erro
    print("Isso não é um número!")
    
# Exemplo com erro propositado:
try:
    numero = int("abc")
except ValueError:
    print("Erro apanhado! 'abc' não é um número válido.")
print()


# ──────────────────────────────────────────────
# 3. INPUT SEGURO (pattern reutilizável)
# ──────────────────────────────────────────────
# Esta função resolve o problema principal do teu math.py:
# o programa não crasha mais com input inválido.

print("=== 3. INPUT SEGURO ===")


def obter_input(texto, tipo=int):
    """
    Pede input ao utilizador e repete até receber um valor válido.

    Parâmetros:
        texto (str): mensagem mostrada ao utilizador
        tipo (type): tipo pretendido (int, float, Decimal)
    """
    while True:
        try:
            return tipo(input(texto))
        except ValueError:
            print("  Input inválido! Tenta novamente.")


# Demonstração - isto NÃO crasha:
# numero = obter_input("Digite um número: ")  # pede até receber um int
# real = obter_input("Digite um decimal: ", float)  # pede até receber float

print("  Função obter_input() criada - ver exemplo no final do ficheiro")
print()


# ──────────────────────────────────────────────
# 4. DICIONÁRIOS E VALIDAÇÃO
# ──────────────────────────────────────────────
# Dicionários guardam pares chave-valor.
# Usar "in" valida se uma chave existe ANTES de aceder.

print("=== 4. DICIONÁRIOS ===")

TAXAS = {
    "EUR": 1.0000,
    "USD": 1.0925,
    "BRL": 5.4530,
    "GBP": 0.8560,
}

# MAU - crasha se chave não existir:
# valor = 100 / TAXAS["XYZ"]  # ← KeyError!

# BOM - valida primeiro:
codigo = "USD"
if codigo in TAXAS:
    print(f"  Taxa {codigo}: {TAXAS[codigo]}")
else:
    print(f"  Moeda {codigo} não existe")

# Iterar sobre todas as moedas:
print("  Moedas disponíveis:", list(TAXAS.keys()))
print()


# ──────────────────────────────────────────────
# 5. BOAS PRÁTICAS
# ──────────────────────────────────────────────

print("=== 5. BOAS PRÁTICAS ===")

# ── 5a. Código morto - else inacessível ──
# No teu math.py, isto existe:
#
#   if unidade_temp == 1:
#       ...
#   elif unidade_temp == 2:
#       ...
#   else:              # ← ESTE ELSE NUNCA EXECUTA
#       print("Error")   porque a validação já apanha valores fora do range
#
# CORRETO - validar no início e retornar:
print("  5a. Código morto removido")

# ── 5b. if __name__ == "__main__" ──
# Isto garante que o código só executa quando corres o ficheiro diretamente.
# Se outro ficheiro fizer "import python_fundamentos", não executa o menu.
print("  5b. if __name__ == '__main__' garante execução apenas ao correr diretamente")

# ── 5c. Imports no topo ──
# TODOS os imports devem estar no início do ficheiro, nunca no meio.
print("  5c. Imports sempre no topo do ficheiro")

# ── 5d. Evitar continue desnecessário ──
# No teu math.py:
#
#   while True:
#       ...
#       if escolha == "sair":
#           break
#       else:
#           continue  # ← DESNECESSÁRIO, o loop continua sozinho
#
print("  5d. 'continue' é implícito no final de um loop while")
print()


# ──────────────────────────────────────────────
# 6. EXERCÍCIO GUIADO - Refatorar o math.py
# ──────────────────────────────────────────────
# Aplica tudo o que aprendeste acima.
# Abaixo está o passo a passo de como ficaria o teu conversor.

print("=== 6. EXERCÍCIO - CONVERSOR REFATORADO ===")
print("  (executa esta secção para ver o conversor a funcionar)\n")


from decimal import Decimal


def obter_input(texto, tipo=int):
    """Input seguro que repete até receber valor válido."""
    while True:
        try:
            return tipo(input(texto))
        except ValueError:
            print("  Input inválido! Tenta novamente.")


def converter_distancia():
    """Converte entre km, m e cm."""
    print("\n  1. km → m")
    print("  2. m → km")
    print("  3. m → cm")

    op = obter_input("  Unidade (1-3): ")
    if op not in (1, 2, 3):
        print("  Opção inválida!")
        return

    valor = obter_input("  Valor: ", float)

    if op == 1:
        print(f"  {valor}km = {valor * 1000}m")
    elif op == 2:
        print(f"  {valor}m = {valor / 1000}km")
    else:
        print(f"  {valor}m = {valor * 100}cm")


def converter_temperatura():
    """Converte entre Celsius e Fahrenheit."""
    print("\n  1. Celsius → Fahrenheit")
    print("  2. Fahrenheit → Celsius")

    op = obter_input("  Unidade (1-2): ")
    if op not in (1, 2):
        print("  Opção inválida!")
        return

    valor = obter_input("  Valor: ", float)

    if op == 1:
        print(f"  {valor}ºC = {(valor * 1.8) + 32:.2f}ºF")
    else:
        print(f"  {valor}ºF = {(valor - 32) / 1.8:.2f}ºC")


def converter_massa():
    """Converte entre kg, g e mg."""
    print("\n  1. kg → g")
    print("  2. g → kg")
    print("  3. g → mg")

    op = obter_input("  Unidade (1-3): ")
    if op not in (1, 2, 3):
        print("  Opção inválida!")
        return

    valor = obter_input("  Valor: ", float)

    if op == 1:
        print(f"  {valor}kg = {valor * 1000}g")
    elif op == 2:
        print(f"  {valor}g = {valor / 1000}kg")
    else:
        print(f"  {valor}g = {valor * 1000}mg")


def converter_moeda():
    """Converte entre moedas usando taxas fixas."""
    TAXAS = {
        "EUR": Decimal("1.0000"),
        "USD": Decimal("1.0925"),
        "BRL": Decimal("5.4530"),
        "GBP": Decimal("0.8560"),
    }

    print(f"\n  Moedas: {list(TAXAS.keys())}")

    valor = obter_input("  Valor: ", Decimal)
    origem = input("  Origem: ").upper().strip()
    destino = input("  Destino: ").upper().strip()

    if origem not in TAXAS:
        print(f"  Moeda '{origem}' não existe!")
        return
    if destino not in TAXAS:
        print(f"  Moeda '{destino}' não existe!")
        return

    resultado = (valor / TAXAS[origem] * TAXAS[destino]).quantize(Decimal())
    print(f"  Resultado: {resultado} {destino}")


def menu_principal():
    """Mostra o menu e despacha para a conversão correta."""
    print("===== Conversor de Unidades =====")
    print("  1. Distância")
    print("  2. Temperatura")
    print("  3. Massa")
    print("  4. Moeda")

    op = obter_input("  O que queres converter: ")

    if op == 1:
        converter_distancia()
    elif op == 2:
        converter_temperatura()
    elif op == 3:
        converter_massa()
    elif op == 4:
        converter_moeda()
    else:
        print("  Opção inválida!")


def main():
    """Loop principal do conversor."""
    while True:
        menu_principal()
        escolha = input("\n  Enter para continuar ou 'sair' para sair: ")
        if escolha == "sair":
            print("  Até logo!")
            break


if __name__ == "__main__":
    main()
