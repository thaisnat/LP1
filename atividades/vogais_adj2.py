# coding: utf-8
# Unidade 4 - Vogais Adjacentes (Questão do Miniteste)
# Thaís Nicoly - UFCG 2015.1 - realizado dia 29/05/2015

n = int(raw_input())

n_adjacentes = 0
for i in range(n):
	palavra = raw_input()
	for i in range(len(palavra) -1):
		if palavra[i] in 'aeiou' and palavra[i +1] in 'aeiou':
			n_adjacentes += 1
			break
print n_adjacentes
