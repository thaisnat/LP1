# coding: utf-8
# Unidade 4 - Soma elementos a cada K posições
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

k = int(raw_input())
n = int(raw_input())

numeros = []
soma = 0

for i in range(n):
	numero = int(raw_input())
	numeros.append(numero)

for x in range(0,len(numeros),k):
	soma += numeros[x]
	
print 'Soma: %d.' % soma
