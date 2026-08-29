# =============================================================================
# LISTA DE EXERCÍCIOS PYTHON - NÍVEL MÉDIO (Estilo LeetCode)
# Temas: Variáveis, Operadores, Strings, Estruturas de Dados, Fluxo de Controle
# =============================================================================
# Instruções: Implemente cada função abaixo. Não altere a assinatura.
# Execute o arquivo para rodar os testes de verificação no final.
# =============================================================================


# =============================================================================
# PARTE 1 — VARIÁVEIS E OPERADORES
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# Exercício 1: "Soma dos Dígitos de um Inteiro" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dado um inteiro não negativo n, retorne a soma dos seus dígitos.
# Exemplo:
#   Entrada: n = 12345
#   Saída: 15  (porque 1 + 2 + 3 + 4 + 5 = 15)
# Restrições: 0 <= n <= 10^9
# Não use conversão direta para string (use apenas operadores aritméticos).
# ─────────────────────────────────────────────────────────────────────────────
def soma_digitos(n: int) -> int:
    """TODO: implemente a função soma_digitos usando apenas operadores % e //."""
    # resultado = 0
    # while n > 0:
    #     resultado += n % 10
    #     n //= 10
    # return resultado
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 2: "Conversão de Temperatura Composta" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma temperatura em Fahrenheit, retorne uma tupla (celsius, kelvin)
# arredondada para 2 casas decimais.
# Fórmulas:
#   C = (F - 32) * 5/9
#   K = C + 273.15
# Exemplo:
#   Entrada: fahrenheit = 212.0
#   Saída: (100.0, 373.15)
# ─────────────────────────────────────────────────────────────────────────────
def converte_temperatura(fahrenheit: float) -> tuple[float, float]:
    """TODO: implemente a conversão de Fahrenheit para Celsius e Kelvin."""
    # celsius = (fahrenheit - 32) * 5 / 9
    # kelvin = round(celsius + 273.15, 2)
    # return (round(celsius, 2), kelvin)
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 3: "Divisão Inteira Sem Operador" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dados dois inteiros dividendo e divisor, retorne o quociente da divisão
# inteira (truncado em direção a zero) SEM usar os operadores *, / ou %.
# Exemplo:
#   Entrada: dividendo = 17, divisor = 5
#   Saída: 3
# Exemplo:
#   Entrada: dividendo = -7, divisor = 3
#   Saída: -2
# Restrições: divisor != 0
# ─────────────────────────────────────────────────────────────────────────────
def divisao_inteira(dividendo: int, divisor: int) -> int:
    """TODO: implemente a divisão inteira sem usar *, / ou %."""
    # sinal = -1 if (dividendo < 0) ^ (divisor < 0) else 1
    # dividendo, divisor = abs(dividendo), abs(divisor)
    # quociente = 0
    # while dividendo >= divisor:
    #     dividendo -= divisor
    #     quociente += 1
    # return sinal * quociente
    pass


# =============================================================================
# PARTE 2 — MANIPULAÇÃO DE STRINGS
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# Exercício 4: "Verificação de Palíndromo com Tratamento" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma string s, retorne True se ela é um palíndromo após converter todas
# as letras para minúsculas e remover todos os caracteres que NÃO são
# alfanuméricos (a-z, A-Z, 0-9). Caso contrário, retorne False.
# Um palíndromo é uma frase que se lê da mesma forma de trás para frente.
# Exemplo:
#   Entrada: s = "A man, a plan, a canal: Panama"
#   Saída: True  (pois "amanaplanacanalpanama" é palíndromo)
# Exemplo:
#   Entrada: s = "race a car"
#   Saída: False
# ─────────────────────────────────────────────────────────────────────────────
def eh_palindromo(s: str) -> bool:
    """TODO: implemente a verificação de palíndromo com tratamento."""
    # filtrada = ''.join(c.lower() for c in s if c.isalnum())
    # return filtrada == filtrada[::-1]
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 5: "Comprime a String" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma string s composta por letras minúsculas, retorne uma string
# comprimida no formato "caractere<quantidade>" apenas para caracteres
# que aparecem consecutivamente mais de 1 vez. Caracteres que aparecem
# apenas uma vez consecutivamente devem ser mantidos sem número.
# Se a string comprimida não for menor que a original, retorne a original.
# Exemplo:
#   Entrada: s = "aaabbcdddd"
#   Saída: "a3b2cd4"  (comprida: 7 < original: 10)
# Exemplo:
#   Entrada: s = "abc"
#   Saída: "abc"  (compressão resultaria em "abc", mesma tamanho)
# ─────────────────────────────────────────────────────────────────────────────
def comprime_string(s: str) -> str:
    """TODO: implemente a compressão de string consecutiva."""
    # if not s:
    #     return s
    # resultado = []
    # count = 1
    # for i in range(1, len(s)):
    #     if s[i] == s[i - 1]:
    #         count += 1
    #     else:
    #         resultado.append(s[i - 1])
    #         if count > 1:
    #             resultado.append(str(count))
    #         count = 1
    # resultado.append(s[-1])
    # if count > 1:
    #     resultado.append(str(count))
    # comprimida = ''.join(resultado)
    # return comprimida if len(comprimida) < len(s) else s
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 6: "Inverter Ordem das Palavras" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma string s que contém várias palavras separadas por espaços, retorne
# a string com a ordem das palavras invertida.
# IMPORTANTE: Remova espaços extras no início, no fim e entre palavras
# (deixe apenas um espaço entre cada palavra).
# Exemplo:
#   Entrada: s = "  o céu  é   azul  "
#   Saída: "azul é o céu"
# Exemplo:
#   Entrada: s = "hello   world"
#   Saída: "world hello"
# ─────────────────────────────────────────────────────────────────────────────
def inverte_palavras(s: str) -> str:
    """TODO: implemente a inversão da ordem das palavras."""
    # palavras = s.split()
    # return ' '.join(palavras[::-1])
    pass


# =============================================================================
# PARTE 3 — ESTRUTURAS DE DADOS: LISTAS E TUPLAS
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# Exercício 7: "Maior Produto de Dois Elementos" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma lista de inteiros nums, retorne o maior produto possível entre
# dois elementos distintos da lista (por índice, não por valor).
# Exemplo:
#   Entrada: nums = [3, 4, 5, 2]
#   Saída: 20  (5 * 4)
# Exemplo:
#   Entrada: nums = [-10, -20, 5, 1]
#   Saída: 200  (-10 * -20)
# ─────────────────────────────────────────────────────────────────────────────
def maior_produto(nums: list[int]) -> int:
    """TODO: implemente o maior produto de dois elementos da lista."""
    # nums_sorted = sorted(nums)
    # return max(nums_sorted[-1] * nums_sorted[-2], nums_sorted[0] * nums_sorted[1])
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 8: "Mesclar Listas Ordenadas" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dadas duas listas ordenadas em ordem crescente list1 e list2, retorne
# uma única lista mesclada e ordenada em ordem crescente.
# NÃO use sort() ou sorted() — implemente o merge manualmente.
# Exemplo:
#   Entrada: list1 = [1, 3, 5], list2 = [2, 4, 6]
#   Saída: [1, 2, 3, 4, 5, 6]
# Exemplo:
#   Entrada: list1 = [1, 2, 3], list2 = []
#   Saída: [1, 2, 3]
# ─────────────────────────────────────────────────────────────────────────────
def mesclar_ordenadas(list1: list[int], list2: list[int]) -> list[int]:
    """TODO: implemente o merge manual de duas listas ordenadas."""
    # i, j = 0, 0
    # resultado = []
    # while i < len(list1) and j < len(list2):
    #     if list1[i] <= list2[j]:
    #         resultado.append(list1[i])
    #         i += 1
    #     else:
    #         resultado.append(list2[j])
    #         j += 1
    # resultado.extend(list1[i:])
    # resultado.extend(list2[j:])
    # return resultado
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 9: "Moda em Tupla Estatística" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma tupla de números inteiros nums, retorne uma tupla (moda, frequência)
# onde moda é o elemento que mais aparece. Se houver empate, retorne o menor
# valor entre os empatados.
# Exemplo:
#   Entrada: nums = (1, 3, 3, 2, 2, 2, 3)
#   Saída: (3, 3)
# Exemplo:
#   Entrada: nums = (5, 5, 1, 1, 2)
#   Saída: (1, 2)  (1 e 5 empatam em 2, mas 1 é menor)
# ─────────────────────────────────────────────────────────────────────────────
def moda_tupla(nums: tuple[int, ...]) -> tuple[int, int]:
    """TODO: implemente a busca da moda em uma tupla."""
    # frequencias = {}
    # for n in nums:
    #     frequencias[n] = frequencias.get(n, 0) + 1
    # max_freq = max(frequencias.values())
    # moda = min(k for k, v in frequencias.items() if v == max_freq)
    # return (moda, max_freq)
    pass


# =============================================================================
# PARTE 4 — ESTRUTURAS DE DADOS: SETS E DICIONÁRIOS
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# Exercício 10: "Interseção de Dois Arrays Sem Duplicatas" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dados dois arrays nums1 e nums2, retorne uma lista com a interseção entre
# eles (elementos que aparecem em ambos). Cada elemento no resultado deve ser
# único (sem duplicatas). A ordem do resultado não importa.
# Exemplo:
#   Entrada: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
#   Saída: [2]
# Exemplo:
#   Entrada: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
#   Saída: [9, 4] ou [4, 9]
# ─────────────────────────────────────────────────────────────────────────────
def interseccao(nums1: list[int], nums2: list[int]) -> list[int]:
    """TODO: implemente a interseção usando sets."""
    # return list(set(nums1) & set(nums2))
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 11: "Primeira Inspeção de Caractere Não Repetido" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma string s, encontre o primeiro caractere que NÃO se repete
# (aparece exatamente uma vez) e retorne seu índice. Se não houver, retorne -1.
# Exemplo:
#   Entrada: s = "leetcode"
#   Saída: 0  (o 'l' é o primeiro que não se repete)
# Exemplo:
#   Entrada: s = "aabb"
#   Saída: -1
# ─────────────────────────────────────────────────────────────────────────────
def primeiro_nao_repetido(s: str) -> int:
    """TODO: implemente usando dicionário para contagem de frequência."""
    # freq = {}
    # for c in s:
    #     freq[c] = freq.get(c, 0) + 1
    # for i, c in enumerate(s):
    #     if freq[c] == 1:
    #         return i
    # return -1
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 12: "Agregador de Grupos por Comprimento" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma lista de strings palavras, retorne um dicionário onde cada chave é
# um comprimento e o valor é uma lista de palavras com aquele comprimento.
# As palavras em cada lista devem manter a ordem original de aparecimento.
# Exemplo:
#   Entrada: palavras = ["oi", "python", "é", "hello", "br", "code"]
#   Saída: {2: ["oi", "br"], 6: ["python"], 5: ["hello"], 4: ["code"]}
# ─────────────────────────────────────────────────────────────────────────────
def agrupa_por_comprimento(palavras: list[str]) -> dict[int, list[str]]:
    """TODO: implemente o agrupamento por comprimento usando dicionário."""
    # resultado = {}
    # for p in palavras:
    #     comprimento = len(p)
    #     if comprimento not in resultado:
    #         resultado[comprimento] = []
    #     resultado[comprimento].append(p)
    # return resultado
    pass


# =============================================================================
# PARTE 5 — FLUXO DE CONTROLE: CONDICIONAIS
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# Exercício 13: "Classificador de Jogo de RPG" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Escreva uma função que classifica um personagem de RPG baseado em
# seu nível e classe. Use if/elif/else encadeados.
# Regras:
#   - Se nível < 10: classe = "Novato"
#   - Se 10 <= nível < 30: classe = "Intermediário"
#   - Se nível >= 30: classe = "Avançado"
#
# Bônus por classe:
#   - Se classe for "Avançado" E o personagem for "mago": retorne "Arquimago"
#   - Se classe for "Avançado" E o personagem for "guerreiro": retorne "Cavaleiro"
#   - Se classe for "Intermediário" E o personagem for "mago": retorne "Healer"
#   - Se classe for "Intermediário" E o personagem for "guerreiro": retorne "Brawler"
#   - Caso contrário: retorne a classe base.
# Exemplo:
#   Entrada: nivel = 35, personagem = "mago"
#   Saída: "Arquimago"
# Exemplo:
#   Entrada: nivel = 5, personagem = "guerreiro"
#   Saída: "Novato"
# ─────────────────────────────────────────────────────────────────────────────
def classifica_rpg(nivel: int, personagem: str) -> str:
    """TODO: implemente a classificação com if/elif/else encadeados."""
    # if nivel < 10:
    #     classe = "Novato"
    # elif nivel < 30:
    #     classe = "Intermediário"
    # else:
    #     classe = "Avançado"
    # if classe == "Avançado" and personagem == "mago":
    #     return "Arquimago"
    # if classe == "Avançado" and personagem == "guerreiro":
    #     return "Cavaleiro"
    # if classe == "Intermediário" and personagem == "mago":
    #     return "Healer"
    # if classe == "Intermediário" and personagem == "guerreiro":
    #     return "Brawler"
    # return classe
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 14: "FizzBuzz Estendido" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dado um inteiro n, retorne uma lista de strings de 1 a n seguindo as regras:
#   - Se o número for múltiplo de 3 E de 5: "FizzBuzzPrime" (ex: 15, 30, 45)
#   - Se o número for múltiplo de 3 E um número primo: "FizzPrime"
#   - Se o número for múltiplo de 5 E um número primo: "BuzzPrime"
#   - Se o número for múltiplo de 3: "Fizz"
#   - Se o número for múltiplo de 5: "Buzz"
#   - Se o número for primo: "Prime"
#   - Caso contrário: o número como string
# DICA: Crie uma função auxiliar dentro para verificar se um número é primo.
# Exemplo:
#   Entrada: n = 5
#   Saída: ["Prime", "Prime", "Fizz", "Prime", "Buzz"]
# Exemplo:
#   Entrada: n = 15
#   Saída: ["Prime", "Prime", "Fizz", "Prime", "Buzz", "Fizz", "Prime",
#           "Prime", "Fizz", "Buzz", "Prime", "Fizz", "Prime", "Prime",
#           "FizzBuzzPrime"]
# ─────────────────────────────────────────────────────────────────────────────
def fizzbuzz_extendido(n: int) -> list[str]:
    """TODO: implemente o FizzBuzz estendido com verificação de primalidade."""
    # def eh_primo(x):
    #     if x < 2:
    #         return False
    #     if x == 2:
    #         return True
    #     if x % 2 == 0:
    #         return False
    #     for i in range(3, int(x**0.5) + 1, 2):
    #         if x % i == 0:
    #             return False
    #     return True
    # resultado = []
    # for i in range(1, n + 1):
    #     multiplo3 = i % 3 == 0
    #     multiplo5 = i % 5 == 0
    #     primo = eh_primo(i)
    #     if multiplo3 and multiplo5 and primo:
    #         resultado.append("FizzBuzzPrime")
    #     elif multiplo3 and primo:
    #         resultado.append("FizzPrime")
    #     elif multiplo5 and primo:
    #         resultado.append("BuzzPrime")
    #     elif multiplo3:
    #         resultado.append("Fizz")
    #     elif multiplo5:
    #         resultado.append("Buzz")
    #     elif primo:
    #         resultado.append("Prime")
    #     else:
    #         resultado.append(str(i))
    # return resultado
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Exercício 15: "Calculadora de Notas Escolares com Bônus" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma nota numérica (0-100) e um booleano bonus (se o aluno teve bônus),
# retorne a concepção final da seguinte forma:
#   - Nota >= 90: conceito "A" (ou "A+" se bonus)
#   - 80 <= nota < 90: conceito "B" (ou "B+" se bonus)
#   - 70 <= nota < 80: conceito "C" (ou "C+" se bonus)
#   - 60 <= nota < 70: conceito "D" (ou "D+" se bonus)
#   - nota < 60: conceito "F" (ou "F+" se bonus) — bônus NÃO melhora F
# IMPORTANTE: Use if/elif/else aninhados (nested if) para pelo menos uma
# das condições, não apenas if/elif/else simples encadeados.
# Exemplo:
#   Entrada: nota = 85, bonus = True
#   Saída: "B+"
# Exemplo:
#   Entrada: nota = 92, bonus = False
#   Saída: "A"
# ─────────────────────────────────────────────────────────────────────────────
def conceito_nota(nota: int, bonus: bool) -> str:
    """TODO: implemente com if/elif/else e pelo menos um if aninhado."""
    # if nota >= 90:
    #     if bonus:
    #         return "A+"
    #     return "A"
    # elif nota >= 80:
    #     if bonus:
    #         return "B+"
    #     return "B"
    # elif nota >= 70:
    #     if bonus:
    #         return "C+"
    #     return "C"
    # elif nota >= 60:
    #     if bonus:
    #         return "D+"
    #     return "D"
    # else:
    #     return "F"
    pass


# =============================================================================
# PARTE 6 — EXERCÍCIO BÔNUS (Extra)
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# Exercício 16: "Validador de Senha Strong" (Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Dada uma string senha, retorne True se ela for "forte" segundo as regras:
#   1. Tem pelo menos 8 caracteres.
#   2. Contém pelo menos uma letra minúscula.
#   3. Contém pelo menos uma letra maiúscula.
#   4. Contém pelo menos um dígito.
#   5. Contém pelo menos um caractere especial entre: !@#$%^&*()-+
#   6. NÃO contém espaços.
# Use if/else com curto-circuito (retorne False assim que uma regra falhar)
# e combine operadores lógicos (and, or, not).
# Exemplo:
#   Entrada: senha = "Senha123!"
#   Saída: True
# Exemplo:
#   Entrada: senha = "fraka"
#   Saída: False
# ─────────────────────────────────────────────────────────────────────────────
def valida_senha_forte(senha: str) -> bool:
    """TODO: implemente o validador de senha forte com operadores lógicos."""
    # if len(senha) < 8 or ' ' in senha:
    #     return False
    # tem_minuscula = qualquer(c.islower() para c em senha)
    # tem_maiscula = qualquer(c.isupper() para c em senha)
    # tem_digito = qualquer(c.isdigit() para c em senha)
    # especiais = set('!@#$%^&*()-+')
    # tem_especial = qualquer(c em especiais para c em senha)
    # return tem_minuscula and tem_maiscula and tem_digito and tem_especial
    pass


# =============================================================================
# BLOCO DE TESTES — NÃO ALTERE
# =============================================================================
# Execute: python3 exercicios/teste.py
# Todos os asserts devem passar sem erro para confirmar que a implementação
# está correta.
# =============================================================================

if __name__ == "__main__":

    print("=" * 60)
    print("EXECUTANDO TESTES — PARTE 1: VARIÁVEIS E OPERADORES")
    print("=" * 60)

    # Exercício 1
    assert soma_digitos(12345) == 15, "Falhou: soma_digitos(12345)"
    assert soma_digitos(0) == 0, "Falhou: soma_digitos(0)"
    assert soma_digitos(999) == 27, "Falhou: soma_digitos(999)"
    print("✓ Exercício 1 (soma_digitos) — OK")

    # Exercício 2
    assert converte_temperatura(212.0) == (100.0, 373.15), "Falhou: converte_temperatura(212.0)"
    assert converte_temperatura(32.0) == (0.0, 273.15), "Falhou: converte_temperatura(32.0)"
    print("✓ Exercício 2 (converte_temperatura) — OK")

    # Exercício 3
    assert divisao_inteira(17, 5) == 3, "Falhou: divisao_inteira(17, 5)"
    assert divisao_inteira(-7, 3) == -2, "Falhou: divisao_inteira(-7, 3)"
    assert divisao_inteira(100, 4) == 25, "Falhou: divisao_inteira(100, 4)"
    assert divisao_inteira(7, 3) == 2, "Falhou: divisao_inteira(7, 3)"
    print("✓ Exercício 3 (divisao_inteira) — OK")

    print()
    print("=" * 60)
    print("EXECUTANDO TESTES — PARTE 2: MANIPULAÇÃO DE STRINGS")
    print("=" * 60)

    # Exercício 4
    assert eh_palindromo("A man, a plan, a canal: Panama") is True, "Falhou: eh_palindromo(1)"
    assert eh_palindromo("race a car") is False, "Falhou: eh_palindromo(2)"
    assert eh_palindromo(" ") is True, "Falhou: eh_palindromo(espaço)"
    assert eh_palindromo("Was it a car or a cat I saw") is True, "Falhou: eh_palindromo(3)"
    print("✓ Exercício 4 (eh_palindromo) — OK")

    # Exercício 5
    assert comprime_string("aaabbcdddd") == "a3b2cd4", "Falhou: comprime_string(1)"
    assert comprime_string("abc") == "abc", "Falhou: comprime_string(2)"
    assert comprime_string("aabbcc") == "aabbcc", "Falhou: comprime_string(3)"
    assert comprime_string("") == "", "Falhou: comprime_string(vazio)"
    print("✓ Exercício 5 (comprime_string) — OK")

    # Exercício 6
    assert inverte_palavras("  o céu  é   azul  ") == "azul é o céu", "Falhou: inverte_palavras(1)"
    assert inverte_palavras("hello   world") == "world hello", "Falhou: inverte_palavras(2)"
    assert inverte_palavras("  ") == "", "Falhou: inverte_palavras(espaço)"
    assert inverte_palavras("uma") == "uma", "Falhou: inverte_palavras(uma)"
    print("✓ Exercício 6 (inverte_palavras) — OK")

    print()
    print("=" * 60)
    print("EXECUTANDO TESTES — PARTE 3: LISTAS E TUPLAS")
    print("=" * 60)

    # Exercício 7
    assert maior_produto([3, 4, 5, 2]) == 20, "Falhou: maior_produto(1)"
    assert maior_produto([-10, -20, 5, 1]) == 200, "Falhou: maior_produto(2)"
    assert maior_produto([1, 2]) == 2, "Falhou: maior_produto(3)"
    assert maior_produto([-1, -2, -3, -4]) == 12, "Falhou: maior_produto(4)"
    print("✓ Exercício 7 (maior_produto) — OK")

    # Exercício 8
    assert mesclar_ordenadas([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6], "Falhou: mesclar_ordenadas(1)"
    assert mesclar_ordenadas([1, 2, 3], []) == [1, 2, 3], "Falhou: mesclar_ordenadas(2)"
    assert mesclar_ordenadas([], [1, 2, 3]) == [1, 2, 3], "Falhou: mesclar_ordenadas(3)"
    assert mesclar_ordenadas([1, 1, 3], [2, 3, 4]) == [1, 1, 2, 3, 3, 4], "Falhou: mesclar_ordenadas(4)"
    print("✓ Exercício 8 (mesclar_ordenadas) — OK")

    # Exercício 9
    assert moda_tupla((1, 3, 3, 2, 2, 2, 3)) == (3, 3), "Falhou: moda_tupla(1)"
    assert moda_tupla((5, 5, 1, 1, 2)) == (1, 2), "Falhou: moda_tupla(2)"
    assert moda_tupla((7,)) == (7, 1), "Falhou: moda_tupla(3)"
    assert moda_tupla((4, 4, 4, 2, 2, 2)) == (2, 3), "Falhou: moda_tupla(4)"
    print("✓ Exercício 9 (moda_tupla) — OK")

    print()
    print("=" * 60)
    print("EXECUTANDO TESTES — PARTE 4: SETS E DICIONÁRIOS")
    print("=" * 60)

    # Exercício 10
    resultado = set(interseccao([1, 2, 2, 1], [2, 2]))
    assert resultado == {2}, f"Falhou: interseccao(1) -> {resultado}"
    resultado = set(interseccao([4, 9, 5], [9, 4, 9, 8, 4]))
    assert resultado == {4, 9}, f"Falhou: interseccao(2) -> {resultado}"
    resultado = set(interseccao([1, 2, 3], [4, 5, 6]))
    assert resultado == set(), f"Falhou: interseccao(3) -> {resultado}"
    print("✓ Exercício 10 (interseccao) — OK")

    # Exercício 11
    assert primeiro_nao_repetido("leetcode") == 0, "Falhou: primeiro_nao_repetido(1)"
    assert primeiro_nao_repetido("aabb") == -1, "Falhou: primeiro_nao_repetido(2)"
    assert primeiro_nao_repetido("loveleetcode") == 2, "Falhou: primeiro_nao_repetido(3)"
    assert primeiro_nao_repetido("") == -1, "Falhou: primeiro_nao_repetido(vazio)"
    print("✓ Exercício 11 (primeiro_nao_repetido) — OK")

    # Exercício 12
    resultado = agrupa_por_comprimento(["oi", "python", "é", "hello", "br", "code"])
    esperado = {2: ["oi", "br"], 6: ["python"], 5: ["hello"], 4: ["code"]}
    for k in esperado:
        assert k in resultado and resultado[k] == esperado[k], f"Falhou: agrupa_por_comprimento(1)"
    assert 6 in resultado and resultado[6] == ["python"], "Falhou: chave 6"
    print("✓ Exercício 12 (agrupa_por_comprimento) — OK")

    print()
    print("=" * 60)
    print("EXECUTANDO TESTES — PARTE 5: FLUXO DE CONTROLE")
    print("=" * 60)

    # Exercício 13
    assert classifica_rpg(35, "mago") == "Arquimago", "Falhou: classifica_rpg(1)"
    assert classifica_rpg(35, "guerreiro") == "Cavaleiro", "Falhou: classifica_rpg(2)"
    assert classifica_rpg(5, "guerreiro") == "Novato", "Falhou: classifica_rpg(3)"
    assert classifica_rpg(15, "magro") == "Intermediário", "Falhou: classifica_rpg(4)"
    print("✓ Exercício 13 (classifica_rpg) — OK")

    # Exercício 14
    assert fizzbuzz_extendido(5) == ["Prime", "Prime", "Fizz", "Prime", "Buzz"], "Falhou: fizzbuzz_extendido(5)"
    assert fizzbuzz_extendido(1) == ["Prime"], "Falhou: fizzbuzz_extendido(1)"
    result_15 = fizzbuzz_extendido(15)
    assert result_15[14] == "FizzBuzzPrime", f"Falhou: posição 14 deveria ser FizzBuzzPrime, obtido {result_15[14]}"
    assert result_15[2] == "Fizz", f"Falhou: posição 2 deveria ser Fizz"
    assert result_15[4] == "Buzz", f"Falhou: posição 4 deveria ser Buzz"
    assert result_15[0] == "Prime", f"Falhou: posição 0 deveria ser Prime"
    assert result_15[6] == "Prime", f"Falhou: posição 6 (7 é primo)"
    print("✓ Exercício 14 (fizzbuzz_extendido) — OK")

    # Exercício 15
    assert conceito_nota(85, True) == "B+", "Falhou: conceito_nota(85, True)"
    assert conceito_nota(92, False) == "A", "Falhou: conceito_nota(92, False)"
    assert conceito_nota(92, True) == "A+", "Falhou: conceito_nota(92, True)"
    assert conceito_nota(55, True) == "F", "Falhou: conceito_nota(55, True)"
    assert conceito_nota(72, False) == "C", "Falhou: conceito_nota(72, False)"
    assert conceito_nota(60, True) == "D+", "Falhou: conceito_nota(60, True)"
    print("✓ Exercício 15 (conceito_nota) — OK")

    print()
    print("=" * 60)
    print("EXECUTANDO TESTES — PARTE 6: BÔNUS")
    print("=" * 60)

    # Exercício 16
    assert valida_senha_forte("Senha123!") is True, "Falhou: valida_senha_forte(1)"
    assert valida_senha_forte("fraka") is False, "Falhou: valida_senha_forte(2)"
    assert valida_senha_forte("SENHA123!") is False, "Falhou: valida_senha_forte(3)"
    assert valida_senha_forte("senha123!") is False, "Falhou: valida_senha_forte(4)"
    assert valida_senha_forte("Senha123") is False, "Falhou: valida_senha_forte(5)"
    assert valida_senha_forte("Senha 123!") is False, "Falhou: valida_senha_forte(6)"
    print("✓ Exercício 16 (valida_senha_forte) — OK")

    print()
    print("=" * 60)
    print("TODOS OS TESTES PASSARAM! ✓")
    print("=" * 60)
