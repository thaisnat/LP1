# coding: utf-8
# Unidade 7 - Pivot
# Thaís Nicoly - UFCG 2015.2 - 19/04/2016

def pivot(numeros):
	
	if len(numeros) > 1:
		i = 0
		j = 1
		pivot = numeros[i]
		while j < len(numeros):
			if numeros[j] <= pivot:
				indice_c = i
				fim = j
				while indice_c < fim:
					numeros[fim-1],numeros[fim] = numeros[fim],numeros[fim-1]
					fim -= 1
			j += 1
			if numeros[i] != pivot:
				i += 1

