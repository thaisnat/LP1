# coding: utf-8
# Unidade 4 - Palavras com Letras Dobradas
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

q_palavras = int(raw_input())

tem, nao_tem = 0,0
tem_letra_dobrada = []
nao_tem_dobrada = []

for i in range(q_palavras):
	palavra = raw_input()
	tem_dobrada = False
	for x in range(len(palavra)-1):
		if palavra[x] == palavra[x+1]:
			tem_dobrada = True
	
	if tem_dobrada:
		tem += 1
		tem_letra_dobrada.append(palavra)
	else:
		nao_tem += 1
		nao_tem_dobrada.append(palavra)

print '%d palavra(s) com letras dobradas:' % tem 
for elem in tem_letra_dobrada:
	print elem
print '---'

print '%d palavra(s) sem letras dobradas:' % nao_tem
for elem in nao_tem_dobrada:
	print elem
