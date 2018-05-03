# coding: utf-8
# Unidade 4 - Tentando 'Eh Palindromo'
# Thaís Nicoly - UFCG 2015.2 - 21/03/2016

token = ''
palavra = raw_input()
sim = False

for i in palavra:
	if i != '':
		token += i

for i in range(0,len(token)/2):
	if token[i] == token[-1-i]:
		sim = True
	else:
		sim = False

if sim:
	print 'é'
else:
	print 'não é'
