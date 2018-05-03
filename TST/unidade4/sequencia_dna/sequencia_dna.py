# coding: utf-8
# Unidade 4 - Sequencia de DNA
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

sequencia1 = raw_input()
sequencia2 = raw_input()
cont = 0

for i in range(len(sequencia1)):
	if sequencia1[i] == sequencia2[i]:
			cont += 1
		
if cont > len(sequencia1)/2:
	print 'sim'
else:
	print 'nao'
	
