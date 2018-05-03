# coding: utf-8
# Unidade 5 - Múltiplos de 5
# Thaís Nicoly - UFCG 2015.2 - 12/04/2016

limite = int(raw_input())
while True:
	for i in range(limite-1,-1,-5):
		y = i % 5
		if i == y and y == 0:
			multiplo = i
			break
		
	
	
		

