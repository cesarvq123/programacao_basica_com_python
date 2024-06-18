def contar_espacos(frase):
    contador = 0
    for caractere in frase:
        if caractere == ' ':
            contador += 1
    return contador

def main():
    frase = input("Digite a frase: ")
    espacos = contar_espacos(frase)
    print("Espaços em branco:", espacos)

if __name__ == "__main__":
    main()