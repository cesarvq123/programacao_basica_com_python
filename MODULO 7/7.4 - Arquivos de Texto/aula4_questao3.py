import urllib.request
import os

url = "https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt"
file_name = "estomago.txt"
urllib.request.urlretrieve(url, file_name)

with open(file_name, 'r') as file:
    print(f"Texto das primeiras 25 linhas do arquivo '{file_name}':")
    for i in range(25):
        line = file.readline().rstrip()
        print(line)

    num_lines = sum(1 for line in file)
    print(f"\nNúmero total de linhas do arquivo '{file_name}': {num_lines}")

    max_len = 0
    max_len_line = ""
    for line in file:
        line = line.rstrip()
        if len(line) > max_len:
            max_len = len(line)
            max_len_line = line

    print(f"\nLinha com maior número de caracteres:")
    print(max_len_line)
    print(f"Número de caracteres: {max_len}")

    file.seek(0)
    personagens = ["Nonato", "Íria"]
    count_nonato = 0
    count_iria = 0

    for line in file:
        line_lower = line.lower()
        for personagem in personagens:
            count = line_lower.count(personagem.lower())
            if personagem == "Nonato":
                count_nonato += count
            elif personagem == "Íria":
                count_iria += count

    print(f"\nNúmero de menções aos personagens:")
    print(f"Nonato (e variações): {count_nonato}")
    print(f"Íria (e variações): {count_iria}")

os.remove(file_name)
print(f"\nArquivo '{file_name}' removido.")
