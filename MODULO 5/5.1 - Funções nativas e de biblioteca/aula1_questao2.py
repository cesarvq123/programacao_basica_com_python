import random
import math

n = int(input("Insira o valor de n: "))

soma = 0
for _ in range(n):
    valor_aleatorio = random.randint(0, 100)
    soma += valor_aleatorio
    print(f"Valor aleatório gerado: {valor_aleatorio}")
raiz_quadrada = math.sqrt(soma)

print("A soma dos valores aleatórios é:", soma)
print("A raiz quadrada da soma é:", raiz_quadrada)