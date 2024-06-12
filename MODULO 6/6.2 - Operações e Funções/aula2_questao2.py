import random
num_elemento = random.randint(5 , 20)
elementos = [random.randint (1 , 10) for _ in range(num_elemento)]
soma = sum(elementos)
media = soma / num_elemento
print(elementos)
print(soma)
print(f"{media:.2f}")