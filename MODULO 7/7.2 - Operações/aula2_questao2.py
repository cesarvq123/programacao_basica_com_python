def substituir_vogais_por_asterisco(frase):
    vogais = "aeiouAEIOU"
    nova_frase = ""
    for letra in frase:
        if letra in vogais:
            nova_frase += "*"
        else:
            nova_frase += letra
    return nova_frase

frase = input("Digite uma frase: ")
frase_modificada = substituir_vogais_por_asterisco(frase)
print("Frase modificada:", frase_modificada)
