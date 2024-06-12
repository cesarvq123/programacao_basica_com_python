def listaPar(n):
    return n % 2 == 0
listaPar = [n for n in range(20 , 51) if listaPar(n)]
print(listaPar)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrado = [n**2 for n in lista]
print(quadrado)

lista2 = [x for x in range(1 , 100) if x % 7 == 0]
print(lista2)

def definidor(y):
    if y % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
nomeada = [definidor(y) for y in range(0, 30, 3)]
print(nomeada)