# coding: utf-8
# Unidade 4 - Calcula DV
# Thaís Nicoly - UFCG 2015.2 - 15/03/2016 

digitos = raw_input()
soma_p = 0
soma_i = 0

for i in range(len(digitos)):
	if i % 2 == 0:
		soma_p += int(digitos[i]) 
	else:
		i % 2 == 1
		soma_i += int(digitos[i]) 

digito_verificador = ((soma_p * soma_i) % 11)

if digito_verificador == 10:
	print '%s-X' % digitos
else:
	print '%s-%d' % (digitos,digito_verificador)

