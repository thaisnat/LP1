# coding: utf-8
# Unidade 7 - Cria Senha
# Thaís Nicoly - UFCG 2015.2 - 18/04/2016

while True:
	entrada = raw_input()
	if entrada == '*': break
	palavra,nivel_seguranca = entrada.split()
	
	if nivel_seguranca == 'fraco':
		def criaSenhaFraca(palavra):
			for i in palavra:
				if i in 'oO':
					i = '0'
				if i in 'iILl':
					i = '1'
				if i in 'eE':
					i = '3'
				if i in 'aA':
					i = '4'
				if i in 'bB':
					i = '6'
				if i in 'tT':
					i = '7'
			return palavra
	
	if nivel_seguranca == 'forte':
		def criaSenhaForte(palavra):
			nova_senha = ''
			for i in palavra:
				if criaSenhaFraca(palavra):
					nova_senha += palavra
					
			return nova_senha
		print palavra
		print criaSenhaForte(palavra)
				
