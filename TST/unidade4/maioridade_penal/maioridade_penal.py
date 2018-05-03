# coding: utf-8
# Unidade 4 - Maioridade Penal
# Thaís Nicoly - UFCG 2015.2 - 23/03/2016

nome = raw_input().split()
idade = raw_input().split()

for i in range(len(idade)):
	if int(idade[i]) >= 18:
		print nome[i]
