# coding: utf-8
# Unidade 4 - Verificar se uma string é um palindromo
# Thaís Nicoly - UFCG 2015.1 - 08/06/2015

'''
Esse programa serve para saber se uma palavra é igual a ela mesma só que de tras pra frente
tipo arara, so que existem tambem frases que são desse modelo, com isso temos que criar uma nova string para poder armazenar
a frase sem os espaços e ai sim poder saber se é palindromo ou nao.
'''
token = ''
palavra = raw_input()
palavra_invertida = ''

for i in palavra:
	if i != ' ':
		token += i
		
# Observação ! esse metodo utilizado acima é implementando a função split, que nesse codigo, não pode utilizar!!	
		
for i in range(len(token)-1,-1,-1):
	palavra_invertida += token[i]


if palavra_invertida == token:
	print '%s é palíndromo' % palavra
else:
	print '%s não é palíndromo' % palavra

# utilize a frase 'subi no onibus' como exemplo para entendimento dessa parte da questao		
