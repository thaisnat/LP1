# coding: utf-8
# Unidade 6 - Altera Consecutivos (Inverte 2 a 2)
# Thaís Nicoly - UFCG 2015.2 - 15/04/2016

def inverte2a2(seq):
	if len(seq) % 2 == 1:
		for i in range(0,len(seq)-2,2):
				seq[i], seq[i+1] = seq[i+1], seq[i]
	else:
		for i in range(0,len(seq)-1,2):
				seq[i], seq[i+1] = seq[i+1], seq[i]
		

			

