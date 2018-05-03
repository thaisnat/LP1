# coding: utf-8
# Unidade 4 - Verificar se uma string é um palindromo
# Thaís Nicoly - UFCG 2015.1 - 08/06/2015

token = []
palavra = raw_input()
plvr = True

'''for i in palavra:
	if i != ' ':
		token += i
	else:
		if token != ' ':
			print token
			token = '''''

for i in (len(token)/2 +i):
	if token[i] != token[i+(len(token))/2]:
		plvr = False
	else:
		plvr = False
if plvr == True:
	print '%s é palíndromo' % token
		
