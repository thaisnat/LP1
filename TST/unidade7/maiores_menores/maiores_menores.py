# coding: utf-8
# Unidade 7 - Maiores e Menores
# Thaís Nicoly - UFCG 2015.2 - 19/04/2016

pivot = int(raw_input())
menor = []
maior = []

while True:
	numeros = int(raw_input())
	if numeros < 0: break
	
	if numeros <= pivot:
		menor.append(numeros)
	else:
		maior.append(numeros)
	
print menor
print pivot
print maior
