# coding: utf-8
# Unidade 6 - Letras Alternadas
# Thaís Nicoly - UFCG 2015.2 - 16/04/2016

def letras_alternadas(palavra):
	nova_palavra = ''
	for i in range (0, len(palavra),2):
		nova_palavra += palavra[i]
		
	return nova_palavra

