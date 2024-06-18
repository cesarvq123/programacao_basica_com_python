import re

def eh_palindromo(frase):
    frase = re.sub(r'[^a-zA-Z]', '', frase.lower())
    return frase == frase[::-1]

while True:
    entrada = input("Digite uma frase (digite 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    if eh_palindromo(entrada):
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')
