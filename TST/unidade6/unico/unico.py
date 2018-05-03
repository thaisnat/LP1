# coding: utf-8
# Unidade 6 - Único
# Thaís Nicoly - UFCG 2015.2 - 16/04/2016

def unico(string):
	nova_str = ''
	for i in range(len(string)):
		if string[i] not in nova_str:
			nova_str += string[i]
	
	return nova_str
