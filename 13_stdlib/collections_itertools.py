# collections + itertools

# O que aprender:
# - Counter, defaultdict, deque
# - itertools: islice, chain, groupby

# Counter e count- Counter serve para tudo + dicionario e count serve para tudo menos "dicionario e sets"
from collections import Counter
#em listas
lista = [1, 1, 2, 3, 4, 3]
cnt = Counter(lista) #conta um objeto que apareceu x numa sequencia
print(cnt)

#Em strings
fruta = "banana"
print(fruta.count("a")) #3

#em tuples 
# tupla = (10, 10, 20, 30, 50, 100, 10)
# procura = int(input("oq quer procurar: "))
# print(f"Exisitem: `{tupla.count(procura)}`  {procura} na tupla")

ctr1 = Counter([10, 10, 20, 30, 50, 100, 10])
ctr2 = Counter({1: 2, 2: 3, 3: 1})
ctr3 = Counter("Mestre")
print(ctr1)
print(ctr2)
print(ctr3)

#acessar a elementos do Counter
ctr_list = Counter([1, 2, 2, 2, 3, 5, 3])

print(ctr_list[2])
print(ctr_list[3])
print(ctr_list[5])

#metodos counter

metods = Counter([1, 2, 2, 2, 3, 5, 3, 5])
items = list(metods.elements())
common = metods.most_common(2) 

print(common) #[(2, 3), (3, 2)]  filtra o mais provavel a aceitar o most_common "n"
print(items) #[1, 2, 2, 2, 3, 3, 5]


#aumentar coun manualemente

aumentar= Counter([1, 2, 3, 5])
aumentar [5] += 5 #para 5:6
print("Aumentar:", aumentar)

#subtrair
subtrair = Counter([1, 2, 3, 5, 5, 5, 1, 2])
subtrair.subtract([2, 2, 5, 5])
print("Subtrair: ", subtrair)

#...........................................................
from collections import defaultdict

