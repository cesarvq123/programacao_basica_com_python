import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    frase_embaralhada = []

    for palavra in palavras:
        if len(palavra) > 2:
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            letras_interiores = list(palavra[1:-1])
            random.shuffle(letras_interiores)
            palavra_embaralhada = primeira_letra + ''.join(letras_interiores) + ultima_letra
            frase_embaralhada.append(palavra_embaralhada)
        else:
            frase_embaralhada.append(palavra)

    return ' '.join(frase_embaralhada)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
