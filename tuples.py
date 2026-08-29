empty_tuple = tuple()

tpl = ("item1", "item2", "item3")
print(len(tpl))


fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items ou fruits[0:]



orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)

#Pode se converter um tuple em uma lista e vice versa
tpl = ("item1", "item2", "item3")
lst = list(tpl)
print(lst)


paises = ["Portugal", "França", "Espanha", "Guine-bissau",'Denmark','Finland','Norway','Iceland']
pt, fr, es, gb, *scan = paises
print(pt)
print(fr)
print(es)
print(gb)
print(scan)
