# coding: utf-8
# Unidade 4 - Cálculo do Digito Verificador 
# Thaís Nicoly - UFCG 2015.1 - 08/06/2015

numero_conta = raw_input()
soma_pares = 0
soma_impares = 0

for i in range(len(numero_conta)):
	if i % 2 == 0:
		soma_pares += int(numero_conta[i])
	else:
		soma_impares += int(numero_conta[i])
valor = soma_impares * soma_pares

digito = valor % 11

if digito == 10:
	print '%s-X' % numero_conta
else:
	print '%s-%d' % (numero_conta, digito)
