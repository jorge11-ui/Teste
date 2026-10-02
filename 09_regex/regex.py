# Expressões Regulares

# O que aprender:
# - módulo re
# - padrões (patterns)
# - search / match / findall
# - groups

# Escreve aqui os teus testes:

#RegEx ou expressao regular é uma sequencia de caracteres que formam um padrao de procura,
#pode ser usado para ver se uma string contem um determinado sequencia de padrao
import re

txt = "Ola, esta a chover hoje"
x = re.search("^Ola.*hoje$", txt)

print(x)


