# coding: utf-8
# Unidade 7 - Filtrando Elementos e Alterando uma Lista
# Thaís Nicoly - UFCG 2015.2 - 28/04/2016

def filtra_altera_lista(num, lista):
	for i in range(len(lista)-1,-1,-1):
		if i % num != 0:
			lista.pop(i)
