# coding: utf-8
# Unidade 7 - Merge Sort
# Thaís Nicoly - UFCG 2015.2 - 27/04/2016

# o merge não agrupa pra depois fazer a ordenação
# Ele ja adiciona ordenado
# as duas listas iniciais já estão ordenadas
# l1 = [7,10,20] -> i
# l2 = [1,15,30,31] -> j

# resultado l3 = [1,7,10,15,20,30,31]
# cria uma lista vazia
# o tamanho dessa lista será o somatório do tamanho das duas listas

# comparar cada elemento da lista (qm é maior ? i ou j?)

def merge(l1,l2):
	l3 = []
	# i < len(l1) and j < len(l2)
	i,j = 0,0
	while i < len(l1) and j < len(l2):
		if l1[i] <= l2[j]:
			l3.append(l1[i])
			i += 1
		else:
			l3.append(l2[j])
			j += 1
	if i == len(l1):
		for m in range(j,len(l2)):
			l3.append(l2[m])
	else:
		for m in range(i,len(l1)):
			l3.append(l1[m])
		
	return l3

l1 = [7,10,20] 
l2 = [1,15,30,31]
l3 = [1,2,3]
l4 = [2,3,4]
assert merge(l1,l2) == [1,7,10,15,20,30,31]
assert merge(l3,l4) == [1,2,3,4]
