import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    nomes_criptografados = []
    
    for nome in nomes:
        nome_criptografado = ""
        for char in nome:
            if 33 <= ord(char) <= 126:
                char_criptografado = chr(((ord(char) - 33 + chave_aleatoria) % 94) + 33)
                nome_criptografado += char_criptografado
            else:
                nome_criptografado += char
        nomes_criptografados.append(nome_criptografado)
    
    return nomes_criptografados, chave_aleatoria
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave_aleatoria = encrypt(nomes)
print("Chave de criptografia:", chave_aleatoria)
print("Nomes criptografados:", nomes_criptografados)
