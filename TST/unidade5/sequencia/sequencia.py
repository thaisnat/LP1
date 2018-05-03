# coding: utf-8
# Unidade 5 - Sequência
# Thaís Nicoly - UFCG 2015.2 - 14/04/2015

limite = int(raw_input())

num = 1
soma = 0

if limite != 0:
	while True:
		soma += num
	
		if soma >= limite:
			break
		print num
		num *= 2
