import os

frase = input("Digite uma frase: ")

pasta = 'frase.txt'

with open(pasta, 'w', encoding='utf-8') as file:
    file.write(frase)

pasta_completa = os.path.abspath(pasta)

print(f"Frase salva em {pasta_completa}")
