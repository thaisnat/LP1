# coding: utf-8
# Unidade 4 - Desenhando uma Árvore de Natal
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

num = int(raw_input())

num_o = 1

for n in range(num-1,-1,-1):
	print n*' ' + num_o*'o' 
	num_o += 2
print (num-1)*' ' + 'o'
