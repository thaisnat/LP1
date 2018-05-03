# coding: utf-8
# Unidade 4 - Produzindo uma Senha Segura
# Thaís Nicoly - UFCG 2015.2 - 21/03/2016

senha = raw_input()
nova_senha = ''

for i in range(len(senha)):
	if senha[i] == ' ':
		nova_senha += senha[i]
	else:
		duplica = 2 * senha[i]
		nova_senha += duplica
print nova_senha

# Condição para saber se é uma senha segura ou não		
if len(nova_senha) >=  13:
	print 'senha segura'
else:
	print 'senha insegura'
