# coding: utf-8
# Unidade 4 - Quantidade e Média de Números Pares
# Thaís Nicoly - UFCG 2015.2 - 28/03/2016

q_numeros = int(raw_input())

numeros = []
q_par,soma_par,eh_menor = 0,0,0

for i in range(q_numeros):
	numero = int(raw_input())
	numeros.append(numero)
	
	if numero % 2 == 0:
		q_par += 1
		soma_par += numero
		media_par = 0.0
		media_par = float(soma_par)/ q_par

for x in range(len(numeros)):	
	if numeros[x] < media_par:
		eh_menor += 1

print 'soma: %d' % soma_par
print 'média: %.1f' % media_par
print '%d número(s) abaixo da média' % eh_menor

