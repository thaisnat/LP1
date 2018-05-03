# coding: utf-8
# Unidade 4 - Classifica Letra como Vogal ou Consoante
# Thaís Nicoly - UFCG 2015.2 - 15/03/2016

palavra = raw_input()

for i in range(len(palavra)):
	if palavra[i] in 'AEIOUaeiou':
		print '<%s> sim' % palavra[i]
	else:
		print '<%s> nao' % palavra[i]
