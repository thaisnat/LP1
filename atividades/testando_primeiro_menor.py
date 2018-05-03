# coding: utf-8
# Unidade 7 - Testando - Primeiro Menor
# Thaís Nicoly - UFCG 2015.2 - 09/05/2016
'''
def primeiro_menor(num, numeros):
	i = 0
	while numeros[i] > num:
		i += 1
		valor = i
	if numeros[i] == num:
		print 'sem menores que %d' % num
		return -1
	else:
		print 'primeiro menor que %d: %d' % (num,numeros[i])
		return valor'''
def primeiro_menor(num, numeros):
	i = 0
	while int(numeros[i]) > num:
		i += 1
		valor = i
	if int(numeros[i]) == num:
	    return -1
	else:
	    return valor
	
numeros = '7 5 3 9 11 8'
numero = numeros.split()
num = 3
print primeiro_menor(num,numero)

