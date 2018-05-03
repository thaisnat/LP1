# coding: utf-8
# Unidade 4 - Criação de uma Nova Palavra
# Thaís Nicoly - UFCG 2015.2 - 11/03/2016

palavra_fonte = raw_input()
numero_apoio = raw_input()

n = len(palavra_fonte)
nova_palavra = ''

for i in range(n):
	nova_palavra += (int(numero_apoio[n -i -1]))*(palavra_fonte[i]) + palavra_fonte[i]

print nova_palavra
