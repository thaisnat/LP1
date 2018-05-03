# coding: utf-8
# Unidade 5 - Guerra Baralho
# Thaís Nicoly - UFCG 2015.2 - 12/04/2016

pontos_1,pontos_2,empate = 0,0,0

while True:
	jogador_1,jogador_2 = raw_input().split()
	if int(jogador_1) == 0 and int(jogador_2) == 0:
		break
	if int(jogador_1) > int(jogador_2):
		pontos_1 += 1
	elif int(jogador_2) > int(jogador_1):
		pontos_2 += 1
	else:
		empate += 1
print 'Jogador 1: %d, Jogador 2: %d, Empates: %d' % (pontos_1,pontos_2,empate)
