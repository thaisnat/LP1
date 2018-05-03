# coding: utf-8
# Unidade 4 - Soma os Múltiplos do Primeiro Elemento de uma Lista
# Thaís Nicoly - UFCG 2015.2 - 28/03/2016

numero_referencia = int(raw_input())
soma = 0

for i in range(10):
	numeros = int(raw_input())
	
	if numeros % numero_referencia == 0:
		soma += numeros
		
print soma
