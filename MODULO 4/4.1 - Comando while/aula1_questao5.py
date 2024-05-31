x = int(input("Digite quantas idades irão ser calculadas: "))
soma = 0
cont = 0

while cont < x:
    idade = int(input("Digite as idades das pessoas: "))
    soma += idade
    cont += 1
print(f"A média das idades é {soma/x:.0f} anos")