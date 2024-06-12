import random

def contar_elementos(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = list(set(lista1) & set(lista2))

interseccao.sort()

contagem_lista1 = contar_elementos(lista1)
contagem_lista2 = contar_elementos(lista2)

print("lista1 -", lista1)
print("lista2 -", lista2)
print("Interseccao -", interseccao)

print("Contagem")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem_lista1.get(elemento, 0)}, lista2={contagem_lista2.get(elemento, 0)})")
