# coding: utf-8
# Unidade 4 - Criptografando uma Senha
# Thaís Nicoly - UFCG 2015.2 - 14/03/2016

palavra = raw_input()
senha = palavra[0]
troca = 0

for i in range(1,len(palavra)):
	if palavra[i] in 'aA':
		senha += '4'
		troca += 1
	elif palavra[i] in 'eE':
		senha += '3'
		troca += 1
	elif palavra[i] in 'iI':
		senha += '1'
		troca += 1
	elif palavra[i] in 'oO':
		senha += '0'
		troca += 1
	else:
		senha += palavra[i]
		
print senha,'(%d troca(s))' % troca
