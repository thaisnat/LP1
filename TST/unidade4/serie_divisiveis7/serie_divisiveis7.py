# coding: utf-8
# Unidade 4 - Série: Substitui terminados em 7 ou divisíveis por 7
# Thaís Nicoly - UFCG 2015.2 - 14/03/2016

for i in range(1,102,2):
	if i % 7 == 0 or str(i)[-1] == '7' :
		i = '*'
	print i

        
