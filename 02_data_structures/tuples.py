# Criação de tuples
empty_tuple = tuple()
empty_tuple2 = ()

tpl = ("item1", "item2", "item3")
print(len(tpl))

# Single-element tuple — o trailing comma é obrigatório
single = ("only",)
not_single = ("not", "a", "tuple")
print(single)
print(type(single))
print(type(not_single))

# Frutas
fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[0:]  # mesma coisa que [-4:]
print(all_fruits)

orange_mango = fruits[-3:-1]
orange_to_the_rest = fruits[-3:]
print(orange_mango)
print(orange_to_the_rest)

# Imutabilidade — tuples não permitem alteração depois de serem criados
try:
    fruits[0] = "apple"
except TypeError as e:
    print(f"Erro: {e}")

# Métodos .count()  conta quantas vezes um item aparece dentro de de um lista, tuples e string
# .index() conta a posição em que um item se encontra conta a posição em que um item se encontra
print(fruits.count("banana"))
print(fruits.index("mango"))

# Concatenação e repetição
t1 = ("a", "b")
t2 = ("c", "d")
print(t1 + t2)
print(t1 * 3)

# Membership
print("banana" in fruits)
print("apple" not in fruits)

# Comparação
print(("a", "b") < ("a", "c"))
print(("a", "b") == ("a", "b"))

# Conversão
# Pode-se converter um tuple em uma lista e vice versa
tpl = ("item1", "item2", "item3")
lst = list(tpl)
print(lst)
print(tuple(lst))

# Unpacking
paises = [
    "Portugal",
    "França",
    "Espanha",
    "Guine-bissau",
    "Denmark",
    "Finland",
    "Norway",
    "Iceland",
]
pt, fr, es, gb, *scan = paises
print(pt)
print(fr)
print(es)
print(gb)
print(scan)

# Named tuple
from collections import namedtuple

Pais = namedtuple("Pais", "nome continente populacao")
portugal = Pais("Portugal", "Europa", 10_300_000)
print(portugal)
print(portugal.nome)
print(portugal.continente)
