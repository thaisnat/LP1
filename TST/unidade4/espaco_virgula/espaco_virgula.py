# coding: utf-8
# Unidade 4 - Espaço por Vírgula
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

palavra = raw_input()
inteiro_1 = int(raw_input())
inteiro_2 = int(raw_input())
segunda_parte = []

for j in range(len(palavra)):
	if j >= inteiro_1 and j < inteiro_2:
		segunda_parte.append(palavra[j])

for i in segunda_parte:
	if i == ' ':
		print ',',
	else:
		print i,
