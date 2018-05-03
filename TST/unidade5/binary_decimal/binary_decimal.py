# coding: utf-8
# Unidade 5 - Binary Coded Decimal
# Thaís Nicoly - UFCG 2015.2 - 11/04/2016

primeiro_num = ''
segundo_num = ''

num_decimal1, num_decimal2 = 0,0
while True:
	entrada = raw_input()
	if entrada == 'fim' : break
	
	if len(entrada) < 8 or len(entrada) > 8:
		print 'Tente Novamente.'
		break
	
	
'''
n_binario = raw_input()

n_decimal = 0

for i in range(len(n_binario)-1,-1,-1):
	operador = 2**i
	decimal = int(n_binario[-1-i]) * operador
	n_decimal += decimal
	print '%s * %d = %d' % (n_binario[-1-i],operador,decimal)

print '%s(2) = %s(10)' % (n_binario,n_decimal)''' 
