# ============================================================
# PYTHON - CONDICIONAIS (if / elif / else) (Notas Importantes)
# ============================================================

# ------------------------------------------------------------
# 1. SINTAXE BÁSICA
# ------------------------------------------------------------
# A condição vai SEMPRE depois de 'if' e termina com ':'.
# O bloco é definido por INDENTAÇÃO (não por chaves {}).
# Python usa 4 espaços por nível de indentação (PEP 8).

idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# ------------------------------------------------------------
# 2. elif (else if)
# ------------------------------------------------------------
# Usado para testar múltiplas condições em sequência.
# O primeiro 'if' ou 'elif' verdadeiro executa e o resto é ignorado.

nota = 75

if nota >= 90:
    print("A")
elif nota >= 70:
    print("B")
elif nota >= 50:
    print("C")
else:
    print("F")

# ------------------------------------------------------------
# 3. OPERADORES DE COMPARAÇÃO
# ------------------------------------------------------------
# ==  igual a           !=  diferente de
# <   menor            <=  menor ou igual
# >   maior           >=  maior ou igual
# is  identidade       is not  não é o mesmo objeto

# ------------------------------------------------------------
# 4. OPERADORES LÓGICOS
# ------------------------------------------------------------
# and  -> verdadeiro se TODAS as condições forem verdadeiras
# or   -> verdadeiro se PELO MENOS UMA for verdadeira
# not  -> inverte o valor (negação)

if idade >= 18 and idade < 65:
    print("Adulto em idade ativa")

if not (idade < 18):
    print("Não é menor")

f idade >= 18 and idade < 65:
    print("Adulto em idade ativa")

if not (idade < 18):
    print("Não é menor")

# ------------------------------------------------------------
# 5. VALORES "TRUTHY" E "FALSY"
# ------------------------------------------------------------
# Em Python, toda expressão é avaliada como True ou False.
# oooo:q
#
# São Falsy (considerados False):
#   0, 0.0, "", [], {}, (), set(), None, False
#   oooo:q
#
# Tudo o resto é Truthy.
# oooo:q
#

nome = ""
if nome:          # equivalente a: if nome != ""
    print("Tem nome")
else:
    print("Nome vazio")   # <-- executa

# Boa prática:
#   if x:        em vez de   if x == True:
#   if not x:    em vez de   if x == False:

# ------------------------------------------------------------
# 6. COMPARAR COM None
# ------------------------------------------------------------
# Use 'is' / 'is not' (e não == / !=).
valor = None

if valor is None:
    print("Sem valor")

# ------------------------------------------------------------
# 7. OPERADOR TERNÁRIO (if de uma linha)
# ------------------------------------------------------------
# Sintaxe:  resultado = verdadeiro if condicao else falso

status = "OK" if idade >= 18 else "NÃO OK"
print(status)

# ------------------------------------------------------------
# 8. if encadeado vs aninhado
# ------------------------------------------------------------
# Aninhar (if dentro de if) cria dependência hierárquica:

if idade >= 18:
    if idade >= 65:
        print("Senior")
    else:
        print("Adulto")
else:
    print("Jovem")

# Evite muitos níveis de aninhamento (dificulta leitura).
# Prefira 'elif' ou simplificar a lógica.

# ------------------------------------------------------------
# 9. MATCH-CASE (Python 3.10+) - alternativa ao if/elif
# ------------------------------------------------------------
# Útil para comparar um valor contra vários padrões.

comando = "start"
match comando:
    case "start":
        print("Iniciar")
    case "stop":
        print("Parar")
    case _:                # wildcard (equivalente ao else)
        print("Desconhecido")

# ------------------------------------------------------------
# 10. ERROS COMUNS
# ------------------------------------------------------------
# - Esquecer os ':' no final da condição.
# - Usar '=' (atribuição) em vez de '==' (comparação).
# - Misturar tabs e espaços na indentação (erro de sintaxe).
# - Variável não definida na condição -> NameError.
# - Condições sempre verdadeiras por erro de lógica (and/or mal usados).
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
