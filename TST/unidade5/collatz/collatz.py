# coding: utf-8
# Unidade 5 - A Conjectura de Collatz
# Thaís Nicoly - UFCG 2015.2 - 11/04/2016

num = int(raw_input())

antec = num-1
valor = []
valor.append(num)
while True:
	
	if num % 2 == 0:
		num = num / 2
		valor.append(num)
	else:
		num = 3*num + 1
		valor.append(num)
	if num == 1:
		break

for elem in valor:
	print elem
