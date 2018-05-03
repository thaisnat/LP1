# coding: utf-8
# Unidade 7 - Último Índice
# Thaís Nicoly - UFCG 2015.2 - 12/05/2016

def ultimo_indice(num, lista):
	tem = True
	for i in range(len(lista)-1,-1,-1):
		if lista[i] == num:
			tem = False
			return i
	if tem:
		return -1

