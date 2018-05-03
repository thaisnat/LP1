# coding: utf-8
# Unidade 7 - (teste Pivot)
# Thaís Nicoly - UFCG 2015.2 - 02/05/2016

lista = [5,6,9,2,3,18,21,1]

numero = lista
def pivot(numeros):
	i = 0
	j = 1
	pivot = numeros[i]
	
	while j < len(numeros):
		if numeros[j] < pivot:
			while numeros[j-1] > pivot:
				numeros[j-1],numeros[j] = numeros[j],numeros[j-1]
				j -= 1
		j += 1
	
	x = 0
	y = 1
	while numeros[y] < numeros[x]:
		if numeros[y] < numeros[x]:
			numeros[x],numeros[y] = numeros[y],numeros[x]
			x += 1
		y += 1
	print numeros
	
l = [5,6,9,2,3,18,21,1]
print pivot(l)
