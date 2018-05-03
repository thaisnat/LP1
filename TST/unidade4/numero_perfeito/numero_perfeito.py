# coding: utf-8
# Unidade 4 - Número Perfeito
# Thaís Nicoly - UFCG 2015.2 - 28/03/2016

numero = int(raw_input())
soma = 0

for i in range(1,numero,1):
	if numero % i == 0:
		soma += i

if soma == numero:
	print '%d é um número perfeito.' % numero
else:
	print '%d não é um número perfeito.' % numero
