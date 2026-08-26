# ============================================================
# PYTHON - VARIÁVEIS (Notas Importantes)
# ============================================================

# ------------------------------------------------------------
# 1. O QUE É UMA VARIÁVEL?
# ------------------------------------------------------------
# Uma variável é um nome que referencia (aponta para) um objeto
# na memória. Em Python, variáveis são "etiquetas" (labels),
# não "caixas" que guardam valores.

# ------------------------------------------------------------
# 2. DECLARAÇÃO E ATRIBUIÇÃO
# ------------------------------------------------------------
# Não precisa declarar tipo. O Python infere automaticamente.
nome = "Joana"          # str
idade = 25              # int
altura = 1.68           # float
ativo = True            # bool
dados = None            # NoneType

# Atribuição múltipla (tuple unpacking):
x, y, z = 1, 2, 3

# Atribuição do mesmo valor a várias variáveis:
a = b = c = 0

# Swap (trocando valores sem variável temporária):
a, b = b, a

# ------------------------------------------------------------
# 3. REGRAS DE NOMENCLATURA
# ------------------------------------------------------------
# - Deve começar com letra (ou underscore _)
# - Pode conter letras, números e underscore
# - Case-sensitive: 'nome' != 'Nome' != 'NOME'
# - NÃO pode ser palavra reservada do Python
#   (if, else, for, while, class, def, import, return, etc.)

# Convenções (PEP 8):
# - Variáveis e funções: snake_case (minúscula com underscore)
#   nome_completo = "Maria"
# - Constantes: UPPER_SNAKE_CASE
#   PI = 3.14159
#   MAX_TENTATIVAS = 3
# - Classes: PascalCase (CamelCase)
#   class MinhaClasse:

# ------------------------------------------------------------
# 4. DINAMICAMENTE TIPOADA (Duck Typing)
# ------------------------------------------------------------
# Uma variável pode mudar de tipo durante a execução:
x = 10          # int
x = "texto"     # agora é str (sem erro!)
x = [1, 2, 3]   # agora é list

# Isso é diferente de C/Java/TypeLang onde o tipo é fixo.

# ------------------------------------------------------------
# 5. VERIFICANDO O TIPO
# ------------------------------------------------------------
# use type() para verificar:
print(type(nome))       # <class 'str'>
print(type(idade))      # <class 'int'>

# use isinstance() (mais recomendado para verificações):
print(isinstance(idade, int))   # True

# ------------------------------------------------------------
# 6. ESCOPO DAS VARIÁVEIS (SCOPE)
# ------------------------------------------------------------
# - Local: dentro de uma função
# - Enclosing: dentro de uma função aninhada
# - Global: no nível do módulo/arquivo
# - Built-in: nomes pré-definidos do Python (print, len, etc.)

contador = 0  # global

def incrementar():
    global contador   # acessa a global
    contador += 1

# Usar 'global' excessivamente é má prática.
# Prefira passar valores como parâmetro e retornar resultados.

# ------------------------------------------------------------
# 7. MUTÁVEL vs IMUTÁVEL
# ------------------------------------------------------------
# Imutáveis (o valor NÃO pode ser alterado após criação):
#   int, float, complex, bool, str, tuple, frozenset, bytes
# Mutáveis (o valor PODE ser alterado):
#   list, dict, set, bytearray, objetos customizados

# Exemplo importante com mutável:
lista_a = [1, 2, 3]
lista_b = lista_a        # ambas apontam para o MESMO objeto!
lista_b.append(4)
print(lista_a)           # [1, 2, 3, 4] -- lista_a também mudou!

# Para criar uma cópia independente:
lista_c = lista_a.copy()      # cópia rasa (shallow)
lista_d = lista_a[:]          # slicing também cria cópia
import copy
lista_e = copy.deepcopy(lista_a)  # cópia profunda (deep)

# ------------------------------------------------------------
# 8. IDENTIDADE vs IGUALDADE
# ------------------------------------------------------------
# == verifica se os VALORES são iguais (igualdade)
# is verifica se são o MESMO OBJETO na memória (identidade)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  (mesmos valores)
print(a is b)   # False (objetos diferentes na memória)
print(a is c)   # True  (mesmo objeto)

# Dica: use 'is' para comparar com None:
#   if x is None:   <-- CORRETO
#   if x == None:   <-- evite

# ------------------------------------------------------------
# 9. BUILTINS ÚTEIS PARA VARIÁVEIS
# ------------------------------------------------------------
# id(var)        -> retorna o endereço/identidade do objeto
# type(var)      -> retorna o tipo
# isinstance()   -> verifica o tipo (aceita tupla de tipos)
# del var        -> deleta a variável
# dir()          -> lista atributos/métodos disponíveis
# help()         -> documentação
# vars()         -> dicionário __dict__ do objeto

# ------------------------------------------------------------
# 10. UNPACKING E *OPERADORES
# ------------------------------------------------------------
# Unpacking com restante:
primeiro, *meio, ultimo = [1, 2, 3, 4, 5]
# primeiro = 1, meio = [2, 3, 4], ultimo = 5

# Troca de valores:
x, y = 10, 20
x, y = y, x    # x=20, y=10

# ------------------------------------------------------------
# 11. AIS (ALIASING)
# ------------------------------------------------------------
# Criar um alias (apelido) para o mesmo objeto:
nomes = ["Ana", "Bia"]
amigos = nomes  # alias - mesmo objeto na memória

# Para evitar efeitos colaterais, use cópia:
amigos = nomes.copy()

# ------------------------------------------------------------
# 12. PASS by ASSIGNMENT (como Python passa argumentos)
# ------------------------------------------------------------
# Python NÃO passa por valor nem por referência.
# Passa por "assignment" (apelido):
#   - Imutáveis: comportam-se como pass-by-value
#   - Mutáveis: mudanças dentro da função afetam o original

def modificar(lista):
    lista.append(99)  # afeta o original!

def atribuir(lista):
    lista = [99, 88]  # NÃO afeta o original (reatribuição local)

nums = [1, 2, 3]
modificar(nums)
print(nums)        # [1, 2, 3, 99]

atribuir(nums)
print(nums)        # [1, 2, 3, 99] -- não mudou

# ------------------------------------------------------------
# 13. TIPOS ESPECIAIS
# ------------------------------------------------------------
# complex:
z = 3 + 4j
print(z.real)   # 3.0
print(z.imag)   # 4.0

# bytes:
b = b"hello"

# None (único valor do tipo NoneType):
resultado = None
if resultado is None:
    print("Sem resultado")

# ------------------------------------------------------------
# 14. F-STRINGS E FORMATAÇÃO (relacionado a variáveis)
# ------------------------------------------------------------
nome = "Python"
versao = 3.12
print(f"{nome} versão {versao}")      # f-string (3.6+)
print(f"{nome:>10}")                   # alinhamento à direita
print(f"{versao:.1f}")                 # 1 casa decimal
print(f"{255:#010b}")                 # binário: 0b11111111

# ------------------------------------------------------------
# 15. CONSTANTES (convenção, não enforced pelo interpreter)
# ------------------------------------------------------------
# Python NÃO tem constantes reais. Usamos UPPER_CASE por
# convenção, mas o interpreter permite alterar o valor.
PI = 3.14159
PI = "alterado"  # funciona, mas NÃO faça isso!

# Para constante real, use módulo 'const' ou enums.
