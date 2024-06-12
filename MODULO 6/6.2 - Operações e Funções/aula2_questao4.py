def intercalar_listas(lista1, lista2):
    intercalada = []
    tamanho_min = min(len(lista1), len(lista2))
    for i in range(tamanho_min):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])

    if len(lista1) > len(lista2):
        intercalada.extend(lista1[tamanho_min:])
    elif len(lista2) > len(lista1):
        intercalada.extend(lista2[tamanho_min:])

    return intercalada

quantidade_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o {i+1}º elemento da lista 1: ")) for i in range(quantidade_lista1)]

quantidade_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o {i+1}º elemento da lista 2: ")) for i in range(quantidade_lista2)]

lista_intercalada = intercalar_listas(lista1, lista2)

print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))
