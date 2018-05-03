# coding: utf-8
# Unidade 4 - Divisores Próprios Pares
# Thaís Nicoly - UFCG 2015.2 - 14/03/2016

numero = int(raw_input())

for i in range(2,numero):
	if numero % i == 0 and i % 2 == 0:
		print i
		
	
