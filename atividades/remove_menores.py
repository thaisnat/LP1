# coding: utf-8
# Unidade 8 - Remove Menores de uma Lista
# Thaís Nicoly - UFCG 2015.2 - 12/05/2016

def remove_menores(N, lista):
	cont = 0
	for i in range(len(lista)-1,-1,-1):
		if lista[i] < N:
			cont += 1
			lista.pop(i)
			
	return cont

lista = [1,2,3,4,5]
assert remove_menores(3,lista) == 2
assert lista == [3, 4, 5]
