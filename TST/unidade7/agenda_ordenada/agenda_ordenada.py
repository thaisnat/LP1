# coding: utf-8
# Unidade 7 - Agenda Ordenada
# Thaís Nicoly - UFCG 2015.2 - 18/04/2016

agenda  = [] 
while True:
	nome = raw_input()
	if nome == '####': break
	agenda.append(nome)
	
	for x in range(len(agenda)):
		for i in range(len(agenda)-1):
			if agenda[i][0] > agenda[i+1][0]:
				agenda[i+1],agenda[i] = agenda[i],agenda[i+1]
			
	for elem in agenda:
		if elem == nome:
			print '* %s' % elem
		else:
			print elem
	print '----'



