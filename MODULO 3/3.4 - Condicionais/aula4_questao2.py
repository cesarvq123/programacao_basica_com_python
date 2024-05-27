estrela = int(input("Digite a avaliação em estrelas de algum filme: "))
ruim = 1
regular = 2
bom = 3
muito_bom = 4
exelente = 5
qualidade = ruim or regular or bom or muito_bom or exelente
if estrela == ruim or regular or bom or muito_bom or exelente:
    print (f"Esse fimle é {qualidade}")