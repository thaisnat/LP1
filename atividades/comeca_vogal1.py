# coding: utf-8
# Unidade 4 - Como fazer um programa que pede a quantidade de palavras que começam com vogal
# Thaís Nicoly - UFCG 2015.1 - 01/06/2015

# Este programa recebe uma frase 
frase = raw_input()

tokens = frase.split()
comeca_vogais = 0
vogais = []

for i in tokens:
	if i[0] in 'aeiou':
		comeca_vogais +=1
		
print comeca_vogais

'''frase = raw_input().split()
comeca = 0

for i in frase:
	if i[0] in 'aeiou':
		comeca += 1
print comeca'''
