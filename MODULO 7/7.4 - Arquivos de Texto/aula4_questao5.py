import csv

livros = [
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1178],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Quixote", "Miguel de Cervantes", 1605, 863],
    ["A Revolução dos Bichos", "George Orwell", 1945, 144],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["Crime e Castigo", "Fiódor Dostoiévski", 1866, 551],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 279],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
    ["A Metamorfose", "Franz Kafka", 1915, 55],
    ["Moby Dick", "Herman Melville", 1851, 624]
]

with open('meus_livros.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    for livro in livros:
        escritor_csv.writerow(livro)

print("Arquivo 'meus_livros.csv' foi criado com sucesso!")
