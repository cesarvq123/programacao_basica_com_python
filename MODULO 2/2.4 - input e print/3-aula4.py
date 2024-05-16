##Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
##Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).
##A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
##Entrada:
##Digite o nome do produto 1: calça
##Digite o preço unitário do produto 1: 199.90
##Digite a quantidade do produto 1: 3
##Digite o nome do produto 2: camisa
##Digite o preço unitário do produto 2: 49.95
##Digite a quantidade do produto 2: 10
##Digite o nome do produto 3: cinto
##Digite o preço unitário do produto 3: 25
##Digite a quantidade do produto 3: 3

##Saída:
##Total: R$1,174.20

nome_do_produto1 = np1 = (input("Digite o nome do produto 1: "))
preco_do_produto1 = pp1 = float(input("Digite o preço unitário do produto 1: "))
quantidade_do_produto1 = qp1 = int(input("Digite a quantidade do produto 1: "))

nome_do_produto2 = np2 = (input("Digite o nome do produto 2: "))
preco_do_produto2 = pp2 = float(input("Digite o preço unitário do produto 2: "))
quantidade_do_produto2 = qp2 = int(input("Digite a quantidade do produto 2: "))

nome_do_produto3 = np3 = (input("Digite o nome do produto 3: "))
preco_do_produto3 = pp3 = float(input("Digite o preço unitário do produto 3: "))
quantidade_do_produto3 = qp3 = int(input("Digite a quantidade do produto 3: "))

total = (pp1 * qp1) + (pp2 * qp2) + (pp3 * qp3)

print (f"O valor total gasto foi: R$ {total:,.2f}")