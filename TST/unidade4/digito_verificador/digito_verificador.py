# coding: utf-8
# Unidade 4 - Produzindo um Digito Verificador 
# Thaís Nicoly - UFCG 2015.1 - 07/06/2015

numero_conta = raw_input()
soma = 0

for i in range(len(numero_conta)):
	soma += int(numero_conta[i])
	
digito = soma % 11

if digito == 10:
	print '%s-X' % numero_conta
else:
	print '%s-%d' % (numero_conta,digito)
