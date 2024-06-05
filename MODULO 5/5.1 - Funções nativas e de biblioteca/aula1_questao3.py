import random
n = random.randint (1 , 10)

while True:
    m = int(input("Adivinhe o número entre 1 e 10: "))

    if m > n:
        print("Valor mais alto do que o correto, tente novamente")
    elif m < n:
        print("Valor menor do que o correto, tente novamente")
    else:
        print ("Acertou, parabéns!!")
        break