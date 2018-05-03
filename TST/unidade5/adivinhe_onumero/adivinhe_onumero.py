# coding: utf-8
# Unidade 5 - Adivinhe o número
# Thaís Nicoly - UFCG 2015.2 - 14/04/2015

numero = int(raw_input())
cont = 0

while True:
	palpites = int(raw_input('palpite? '))
	cont += 1
	
	if palpites == numero:
		break
	
	if palpites > numero:
		print 'alto'
	else:
		print 'baixo'

print 'Você acertou em %d tentativas.' % cont	
