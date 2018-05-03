# coding: utf-8
# Unidade 7 - Pivot
# Thaís Nicoly - UFCG 2015.2 - 19/04/2016

def pivot(numeros):
	numero = numeros[0]
	for i in range(len(numeros)):
		for j in range(len(numeros)-1):
			if numeros[j] > numero:
				numeros[j],numeros[j+1] = numeros[j+1],numeros[j]
	
	for x in range(1,len(numeros)):
		if numeros[x] < numero:
			numero,numeros[x] = numeros[x],numero
	print numeros
numeros = [6, 4, 8, 1, 7, 3]
pivot(numeros)
assert numeros == [4, 1, 3, 6, 8, 7]
