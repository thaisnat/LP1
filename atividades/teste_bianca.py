# coding: utf-8
# Questão de Bianca

nome = raw_input()

'''cont = 0

for i in range(len(nome)):
	if nome[i] in '3':
		cont += 1
		print 'Nome com problema'

if cont == 0:
	print 'Ok' '''
	
tem = False

for i in nome:
	if i in '3':
		tem = True
		print 'Nome com problema'
		
if tem == False:
	print 'Ok'
		
