# coding: utf-8
# Unidade 5 - Mais Consoantes
# Thaís Nicoly - UFCG 2015.2 - 07/04/2016

lidas = 0

while True:
	palavra = raw_input()
	lidas += 1
	num_vogais,num_consoantes = 0,0
	for i in range(len(palavra)):
		if palavra[i] in 'AaEeIiOoUu':
			num_vogais += 1
		else:
			num_consoantes += 1
	if num_consoantes > num_vogais: break
	
print lidas
	
		
