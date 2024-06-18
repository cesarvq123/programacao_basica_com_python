import os
import sys
input_file_path = 'arquivo_anterior.txt'

output_file_path = 'palavras.txt'

def is_alpha(char):
    return char.isalpha() or char in 'ÁÉÍÓÚáéíóúÂÊÎÔÛâêîôû'

def process_text(content):
    words = []
    current_word = []
    for char in content:
        if is_alpha(char):
            current_word.append(char)
        else:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
    if current_word:  # adiciona a última palavra se houver
        words.append(''.join(current_word))
    return words

with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

words = process_text(content)

with open(output_file_path, 'w', encoding='utf-8') as file:
    for word in words:
        file.write(word + '\n')

with open(output_file_path, 'r', encoding='utf-8') as file:
    print(file.read())
