# coding: utf-8
# Unidade 4 - Imprime Primeira Vogal
# Thaís Nicoly - UFCG 2015.2 - 15/03/2016

palavra = raw_input()
cont = 0

for i in range(len(palavra)):
	if palavra[i] in 'aeiouAEIOU':
		print palavra[i]
		cont += 1
		break
		
if cont == 0:
	print '-'
