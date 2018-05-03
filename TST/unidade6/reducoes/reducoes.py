# coding: utf-8
# Unidade 6 - Reduções
# Thaís Nicoly - UFCG 2015.2 - 21/04/2016

def reducoes(l_inteiros):
	new_list = []
	if len(l_inteiros) == 0 or len(l_inteiros) == 1:
		return new_list
		
	for i in range(1,len(l_inteiros)):
		if (l_inteiros[i-1] - l_inteiros[i]) <= 0:
			new_list.append(0)
		elif (l_inteiros[i-1] - l_inteiros[i]) >= 1:
			new_list.append((l_inteiros[i-1] - l_inteiros[i]))
	
	return new_list
