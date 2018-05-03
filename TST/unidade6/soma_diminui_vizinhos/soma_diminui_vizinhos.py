# coding: utf-8
# Unidade 6 - Soma e Diminui Vizinhos!
# Thaís Nicoly - UFCG 2015.2 - 16/04/2016

def soma_diminui_vizinhos(lista):
	if len(lista) >= 1:	
		soma = lista[0]
		for i in range(1,len(lista)):
			if i % 2 == 1:
				soma += lista[i]
			else:
				soma -= lista[i]
	else:
		soma = 0
	return soma
