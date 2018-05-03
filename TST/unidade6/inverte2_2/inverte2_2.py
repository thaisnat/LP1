# coding: utf-8
# Unidade 6 - Inverte 2 a 2 condicional
# Thaís Nicoly - UFCG 2015.2 - 08/04/2016

def inverte2a2_condicional(seq):
	for i in range(0,len(seq)-1,2):
		if seq[i+1] < seq[i]:
			seq[i], seq[i+1] = seq[i+1], seq[i]
	return seq
			
