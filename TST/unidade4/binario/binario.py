# coding: utf-8
# Unidade 4 - Conversão de Número na Base 2 para a Base 10
# Thaís Nicoly - UFCG 2015.2 - 23/03/2015

n_binario = raw_input()

n_decimal = 0

for i in range(len(n_binario)-1,-1,-1):
	operador = 2**i
	decimal = int(n_binario[-1-i]) * operador
	n_decimal += decimal
	print '%s * %d = %d' % (n_binario[-1-i],operador,decimal)

print '%s(2) = %s(10)' % (n_binario,n_decimal)
