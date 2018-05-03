# coding: utf-8
# Unidade 4 - Duplicadas (Questão do Miniteste - 05-06-2015)
# Thaís Nicoly - UFCG 2015.1 - 08/06/2015

lista = raw_input()
tokens = lista.split()
duplicada = True
controle = len(tokens)/2

if len(tokens)/2 == 0:
	for i in range (controle):
		if tokens[i] != tokens[i+(controle)]:
			duplicada = False
else:
	duplicada = False
if not duplicada:
	print lista
else:
	for i in range(len(tokens)/2):
		print tokens[i]
