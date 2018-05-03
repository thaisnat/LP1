# coding: utf-8
# Unidade 6 - Get Itens
# Thaís Nicoly - UFCG 2015.2 - 18/04/2016

def get_items(valores, indices2):
	nova_seq = []
	for elem in indices2:
		for i in range(len(valores)):
			if elem == i:
				nova_seq.append(valores[i])
		if elem >= len(valores):
			nova_seq.append(None)
	
	return nova_seq


