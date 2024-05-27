idade_do_participante = idp = int(input("Informe qual a sua idade: "))
numero_de_jogos = ndj = int(input("Já jogou quantos jogos de tabuleiro? "))
partidas_ganhas = pg = int(input("Informe quantas patidas ganhou: "))
idade_minima = im = idp >= 16 and idp <= 18
partidas_jogadas = pj = ndj >= 3
partidas_vencidas = pv = pg >= 1
apto = im and pj and pv
print (f"Apto para ingressar na partida: {apto}")