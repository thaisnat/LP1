# coding: utf-8
# Unidade 6 - Privilegia Digito (Questão do Miniteste)
# Thaís Nicoly - UFCG 2015.2 - 29/04/2016

def privilegia_digito(lista):
	da_vez = 0
	for i in range(len(lista)):
		if lista[i] % 10 <= 5:
			for j in range(i,da_vez,-1):
				lista[j],lista[j-1] = lista[j-1],lista[j]
			da_vez += 1

