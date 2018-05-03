# coding: utf-8
# Unidade 7 - Z inicial
# Thaís Nicoly - UFCG 2015.2 - 19/04/2016

def z_inicial(lista):
	cont_z = 0
	for i in range(len(lista)):
		if lista[i][0] in 'zZ':
			cont_z += 1
	return cont_z

palavras = raw_input().split()

if z_inicial(palavras):
	print z_inicial(palavras)
else:
	print 0
