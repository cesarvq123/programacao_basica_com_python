n = int(input("Digite a quantidade de experimentos que serão feitos: "))

cont = 0
sapo , coelho , rato = 0 , 0 , 0

while cont < n:
    quantia = int(input("Digite quantia de animais que serão usados no expermento: "))
    tipo = input("Digite o tipo de cobaia (sapo = s , coelho = c , rato = r): ")
    if tipo == "S" or "s":
        sapo += quantia
    elif tipo == "C" or "c":
        coelho += quantia
    elif tipo == "R" or "r":
        rato += quantia
    cont += 1
print(f"Total de cobaias: {sapo + coelho + rato}")
print(f"Total de sapos: {sapo}")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")