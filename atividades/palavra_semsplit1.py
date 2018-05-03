# coding: utf-8
# Unidade 4 - Criar um programa que faz a separação de espaço sem a função 'split'
# Thaís Nicoly - UFCG 2015.1 - 01/06/2015

token = ''
palavra = raw_input()

for i in palavra:
	if i != ' ':
		token += i
	else:
		if token != ' ':
			print token
			token = ''
if token != '':
	print token  
