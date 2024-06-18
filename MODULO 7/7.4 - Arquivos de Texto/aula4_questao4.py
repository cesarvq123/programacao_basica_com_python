import urllib.request
import random
import os

def gabarito():
    palavras = [
        'casa',
        'flor',
        'gato',
        'sol',
        'amor',
        'agua',
        'lapis',
        'ceu',
        'mesa',
        'livro'
    ]
    with open('gabarito_forca.txt', 'w') as arquivo:
        arquivo.write('\n'.join(palavras))

def boneco():
    url = 'https://raw.githubusercontent.com/camilalaranjeira/python-basico-exercicios/main/modulo7/gabarito_enforcado.txt'
    try:
        urllib.request.urlretrieve(url, 'gabarito_enforcado.txt')
    except Exception as e:
        print(f'Erro ao baixar o arquivo: {e}')

def carregar_palavra():
    with open('gabarito_forca.txt', 'r') as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras)

def carregar_enforcado():
    with open('gabarito_enforcado.txt', 'r') as arquivo:
        enforcado = arquivo.read().strip().split('\n\n')
    return enforcado

def inicializar_progresso(palavra):
    return ['_'] * len(palavra)

def imprime_enforcado(erros, enforcado):
    if erros < len(enforcado):
        print(enforcado[erros])
    else:
        print("Erro: estágio do enforcado não encontrado.")

def mostra_progresso(progresso):
    print(' '.join(progresso))

def main():
    gabarito()
    boneco()
    
    palavra_secreta = carregar_palavra()
    enforcado = carregar_enforcado()
    progresso = inicializar_progresso(palavra_secreta)
    tentativas_restantes = 6
    letras_utilizadas = set()

    print("Bem-vindo ao Jogo da Forca!")
    print(f"A palavra secreta tem {len(palavra_secreta)} letras.")
    mostra_progresso(progresso)

    while tentativas_restantes > 0:
        letra = input("Digite uma letra: ").strip().lower()

        if letra in letras_utilizadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        letras_utilizadas.add(letra)

        if letra in palavra_secreta:
            print("Letra correta!")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    progresso[i] = letra
            mostra_progresso(progresso)
        else:
            print("Letra incorreta!")
            imprime_enforcado(6 - tentativas_restantes, enforcado)
            mostra_progresso(progresso)
        
        tentativas_restantes -= 1
        print(f"Tentativas restantes: {tentativas_restantes}")

        if '_' not in progresso:
            print("Parabéns! Você descobriu a palavra secreta:", palavra_secreta)
            break

    if '_' in progresso:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)

    try:
        os.remove('gabarito_forca.txt')
        os.remove('gabarito_enforcado.txt')
        print("Arquivos removidos com sucesso.")
    except FileNotFoundError:
        print("Arquivos não encontrados para remoção.")

if __name__ == "__main__":
    main()