# coding: utf-8
# Unidade 6 - Soma Intervalo
# Thaís Nicoly - UFCG 2015.2 - 21/04/2016

def soma_intervalo(a,b):
	if a <= b:
		soma = 0
		for i in range(a,b+1):
			soma += i
	
	return soma
