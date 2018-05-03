# coding: utf-8
# Unidade 6 - Quantos Comeram?
# Thaís Nicoly - UFCG 2015.2 - 07/04/2016

def quantos_comeram(N, fila):
	soma = 0
	for i in range(-1,len(fila)):
		if N < fila[i]:
			return 0
		soma += fila[i]
	while True:
		if soma > N:
			soma -= fila[-1]
		elif soma <= N:
			return soma

