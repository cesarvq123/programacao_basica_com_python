def escada(nome):
    for i in range(1, len(nome) + 1):
        print(nome[:i])

def main():
    nome = input("Digite seu nome: ")
    escada(nome)

if __name__ == "__main__":
    main()