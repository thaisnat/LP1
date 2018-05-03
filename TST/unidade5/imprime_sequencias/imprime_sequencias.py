# coding: utf-8
# Unidade 5 - Imprime Sequencias de Números Inteiros
# Thaís Nicoly - UFCG 2015.2 - 14/04/2015

numero_alvo = int(raw_input())
numero_sequencia = 1

while True:
	sequencia = raw_input()
	
	if sequencia == 'fim':
		break
	
	seq_inteiros = sequencia.split()
	maiores = 0
	
	for i in seq_inteiros:
		if int(i) > numero_alvo:
			maiores +=1
	
	if maiores > (len(seq_inteiros)/2.0):
		print 'sequencia %d: %s' % (numero_sequencia, sequencia)
	
	numero_sequencia += 1
		
