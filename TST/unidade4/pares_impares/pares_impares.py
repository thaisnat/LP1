# coding: utf-8
# Unidade 4 - Quantidade de Números Pares e Ímpares
# Thaís Nicoly - UFCG 2015.2 - 28/03/2016


q_inteiros = int(raw_input())
q_par,q_impar,soma_par,soma_impar = 0,0,0,0

for i in range(q_inteiros):
	numeros = int(raw_input())
	
	if numeros % 2 == 0:
		q_par += 1
		soma_par += numeros
	else:
		q_impar += 1
		soma_impar += numeros
		
media_par,media_impar = 0.0,0.0	
media_par = soma_par/ q_par
media_impar = soma_impar/q_impar

print 'pares: %d' % q_par
print 'ímpares: %d' % q_impar
print 'média pares: %.1f' % media_par
print 'média ímpares: %.1f' % media_impar

