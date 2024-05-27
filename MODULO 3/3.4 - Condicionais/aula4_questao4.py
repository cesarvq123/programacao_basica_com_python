print("Para calcular seu frete, precisarei saber:")

distancia = int(input("A distância em km: "))
peso = int(input("O peso do pacote: "))
if distancia <= 100:
    frete = peso * 1.0
else:
    if distancia <= 300:
        frete = peso * 1.5
    else:
        frete = peso * 2.0
if peso > 10:
    frete += 10
    


print(f"O frete é de R${frete}")
