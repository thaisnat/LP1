# coding: utf-8
# Unidade 6 - Pré-vogais
# Thaís Nicoly - UFCG 2015.2 - 16/04/2016

def eh_palindromo(palavra):
	token = ''
	sim = False

	for i in palavra:
		if i != ' ':
			token += i

	for i in range(0,len(token)/2):
		if token[i] == token[-1-i]:
			sim = True
		else:
			sim = False
	return sim
			
def pre_vogais(palavra):
	palavra = palavra.lower()
	nova_palavra = []
	for i in range(1,len(palavra)):
		if eh_palindromo(palavra):
			if palavra[i] in 'aeiou':
				nova_palavra.append(palavra[i-1])
				break
		else:
			if palavra[i] in 'aeiou':
				nova_palavra.append(palavra[i-1])
	
	return nova_palavra

