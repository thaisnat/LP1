# coding: utf-8
# Unidade 4 - Produto de Dois Somatórios
# Thaís Nicoly - UFCG 2015.2 - 16/03/2016 

numero = raw_input()

soma_p = 0
soma_i = 0

for i in range(len(numero)):
	if i % 2 == 0:
		soma_p += int(numero[i]) 
	else:
		i % 2 == 1
		soma_i += int(numero[i]) 

produto_digitos = soma_p*soma_i

print '%05.f' % produto_digitos
