# coding: utf-8
# Unidade 7 - insere ordenado
# Thaís Nicoly - UFCG 2015.2 - 28/04/2016

# dá um append
# sai trocando de trás pra frente

# insere_na_posicao_k
# pega um elemento e insere na posição k
# como acha a posição ? vai comparando os indices

def insere_ordenada(lista):
	for j in range(len(lista)-1,0,-1):
		if lista[j-1] > lista[j]:
			lista[j-1],lista[j] = lista[j],lista[j-1]
		else:
			break
	print lista
			
l1 = [2,6,9,11,13,5]
insere_ordenada(l1)
assert l1 == [2, 5, 6, 9, 11, 13]

l2 = [1,2,3,0]
insere_ordenada(l2)
assert l2 == [0, 1, 2, 3]
