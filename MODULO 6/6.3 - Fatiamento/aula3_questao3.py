import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista antes da deleção:")
print(lista)

maior_intervalo = []
inicio_intervalo = 0
for i in range(len(lista)):
    if lista[i] < 0:
        contador_negativos = 1
        for j in range(i + 1, len(lista)):
            if lista[j] < 0:
                contador_negativos += 1
            else:
                break
        if contador_negativos > len(maior_intervalo):
            maior_intervalo = lista[i:i+contador_negativos]
            inicio_intervalo = i

del lista[inicio_intervalo:inicio_intervalo+len(maior_intervalo)]

print("Lista após a deleção do intervalo com a maior quantidade de números negativos:")
print(lista)

