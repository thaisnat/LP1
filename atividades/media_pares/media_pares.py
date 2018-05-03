# coding: utf-8
# Unidade 4 - Quantidade e Média de Números Pares
# Thaís Nicoly - UFCG 2015.1 - 08/06/2015

quantidade_n = int(raw_input())

numeros_total = []
cont_par = 0
cont_menor = 0
soma = 0

for i in range(quantidade_n):
	numeros = int(raw_input())
	numeros_total.append(numeros)
	if numeros % 2 == 0:
		cont_par += 1
		soma += numeros

media_par = float(soma) / cont_par

for i in numeros_total:
	if i < int(media_par):
		cont_menor += 1
		
print 'soma: %d' % soma
print 'média: %.1f' % media_par
print '%d número(s) abaixo da média' % cont_menor

 
