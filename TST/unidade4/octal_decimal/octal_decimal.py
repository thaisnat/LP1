# coding: utf-8
# Unidade 4 - Convertendo um Número Octal em um Número Decimal
# Thaís Nicoly - UFCG 2015.2 - 28/03/2016

numero_octal = raw_input()
soma = 0

for i in range(len(numero_octal)):
	posicao = len(numero_octal)-1-i
	converte = int(numero_octal[i])*8**posicao
	soma += converte
	print '%s * 8^%s = %d' % (numero_octal[i],posicao,converte)
print '%s(8) = %d(10)' % (numero_octal,soma) 
