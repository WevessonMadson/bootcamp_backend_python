def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador([1, 2, 3, "4"]):
    print(i)