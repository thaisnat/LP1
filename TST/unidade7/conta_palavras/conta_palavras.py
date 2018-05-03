# coding: utf-8
# Unidade 7 - Conta Palavras
# Thaís Nicoly - UFCG 2015.2 - 19/04/2016

def conta_palavras(k,palavras):
	conta_k = 0
	seq_palavras = palavras.split(':')
	
	for i in range(len(seq_palavras)):
		if len(seq_palavras[i]) >= k:
			conta_k += 1
	
	return conta_k


