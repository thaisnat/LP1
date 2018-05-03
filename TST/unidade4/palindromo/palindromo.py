# coding: utf-8
# Unidade 4 - Palíndromo
# Thaís Nicoly - UFCG 2015.2 - 22/03/2016

token = ''
palavra = raw_input()
sim = False

for i in palavra:
	if i != ' ':
		token += i

for i in range(0,len(token)/2):
	if token[i] == token[-1-i]:
		sim = True
	else:
		sim = False

if sim:
	print '%s é palíndromo' % palavra
else:
	print '%s não é palíndromo' % palavra
