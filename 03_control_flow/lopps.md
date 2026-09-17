# Exercícios

Aqui ficam os exercícios de Python.

## Como organizar
- Um arquivo `.py` por exercício/desafio.
- Nome descritivo, ex: `fizzbuzz.py`, `adivinha_numero.py`.
- Cada arquivo roda de forma independente.

## Lista de exercícios

---

# Loops

## O que aprender
r `for` loop
- `while` loop
- `break` / `continue`
k `range()`

## Quando usar loops
- Para automatizar e repetir tarefas
- Interação indefinida
- Reduzir a complexidade
- Loop infinito

## While

Pode-se fazer um bloco de código repetir-se muitas vezes com `while`, enquanto a condição da instrução for verdadeira.

Uma instrução `while` consiste em:
1. A palavra `while`
2. Uma condição (True ou False)
3. Dois-pontos (`:`)

As instruções `if` e `while` são semelhantes. A diferença é que `while` executa o bloco de código repetidamente até que a condição deixe de ser verdadeira:

```python
y = 0
while y < 3:
    print("vezes")
    y = y + 1  # altera o valor do y a cada repetição
```

```python
name = ""
while name != "Jorge":
    print("pfv nome")
    name = input(">")
print("obg,", name)
```

```python
fome = 5

while fome > 0:
    print(f"nao estou satisfeito: falta {fome} comida")
    fome -= 1
print("hahaha finalmente estou satisfeito")
```

### While...Else

O bloco `else` de um `while` é executado quando a condição se torna falsa (não é executado se o loop for interrompido com `break`):

```python
coun = 0
while coun < 5:
    print(coun)
    coun += 1
else:
    print(coun)
```

```python
num = 0
while num < 3:
    print(num)
    num += 1
else:
    print("loop terminou normalmente")
# Saída: 0 1 2 "loop terminou normalmente"
```

### Exercício resolvido
Imprimir os primeiros 10 números naturais:

```python
numero = 1
while numero < 11:
    print(numero)
    numero += 1
```

## For loop

O `for` loop percorre os elementos de uma sequência (lista, string, range, etc.).

Sintaxe básica:

```python
for variavel in sequencia:
    bloco de código
```

Exemplo com lista:

```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

Exemplo com string:

```python
letras = "python"
for letra in letras:
    print(letra)
```

### For...Else

Mesmo conceito do `while...else`: o `else` é executado se o loop terminar sem `break`:

```python
for i in range(5):
    if i == 10:  # nunca vai ser verdade, então o else executa
        break
else:
    print("nenhum break foi executado")
```

## Range()

`range()` gera uma sequência de números:
- `range(stop)` → vai de 0 até stop-1
- `range(start, stop)` → vai de start até stop-1
- `range(start, stop, step)` → vai de start até stop-1 com passo

```python
# Imprime 0 a 4
for i in range(5):
    print(i)

# Imprime 2 a 6
for i in range(2, 7):
    print(i)

# Imprime 0, 2, 4, 6, 8 (de 2 em 2)
for i in range(0, 10, 2):
    print(i)

# Imprime 10, 9, 8, 7, 6 (contagem regressiva com step negativo)
for i in range(10, 5, -1):
    print(i)
```

## Break

O `break` interrompe o loop imediatamente quando é executado.

Exemplo: para no número 5

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# Saída: 1 2 3 4
```

Exemplo com while (loop infinito interrompido):

```python
counter = 0
while True:
    counter += 1
    if counter == 3:
        break
    print(counter)
# Saída: 1 2
```

## Continue

O `continue` pula a iteração atual e vai para a próxima.

Exemplo: imprime apenas os pares

```python
for i in range(1, 11):
    if i % 2 != 0:  # se for ímpar, pula
        continue
    print(i)
# Saída: 2 4 6 8 10
```

Exemplo: pula o número 3

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Saída: 1 2 4 5
```

## Loop com enumerate()

`enumerate()` retorna o índice e o valor de cada elemento:

```python
frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"índice {indice}: {fruta}")
```

Pode-se definir o índice inicial:

```python
for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}º: {fruta}")
```

## Loop com zip()

`zip()` combina dois ou mais iteráveis elemento por elemento:

```python
nomes = ["Ana", "Bia", "Carlos"]
notas = [9, 7, 10]
for nome, nota in zip(nomes, notas):
    print(f"{nome} tirou {nota}")
```

## Loop com dicionário

```python
pessoa = {"nome": "Jorge", "idade": 25, "cidade": "Porto"}
```

Percorrer as chaves:

```python
for chave in pessoa:
    print(chave)
```

Percorrer chaves e valores com `.items()`:

```python
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

## Loop aninhado

Um loop dentro de outro. Exemplo: tabuada de multiplicar

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print()  # linha em branco entre cada tabuada
```

## List comprehension

Forma reduzida de criar listas com loops.

Forma normal:

```python
quadrados = []
for x in range(1, 6):
    quadrados.append(x ** 2)
```

Com list comprehension (mesmo resultado, mais compacto):

```python
quadrados = [x ** 2 for x in range(1, 6)]
```

Com condição:

```python
pares = [x for x in range(1, 11) if x % 2 == 0]
`
