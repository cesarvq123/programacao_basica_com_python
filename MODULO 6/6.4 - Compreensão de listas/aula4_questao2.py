import string

v = 'aeiouAEIOU'
c = ''.join([p for p in string.ascii_letters if p not in v])

frase = input("Digite uma frase: ")

lista_vogais = sorted([p for p in frase if p in v])
lista_consoantes = [p for p in frase if p in c]

print(f"Vogais: {lista_vogais}")
print(f"Consoantes: {lista_consoantes}")
