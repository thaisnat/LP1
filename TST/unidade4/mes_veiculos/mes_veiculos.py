# coding: utf-8
# Unidade 4 - Mês para Licenciamento de Veículos 
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

placas = raw_input().split()

for i in range(len(placas)):
	if placas[i][-1] == '1' or placas[i][-1] == '2':
		print '%s: janeiro' % placas[i]
	elif placas[i][-1] == '3' or placas[i][-1] == '4':
		print '%s: fevereiro' % placas[i]
	elif placas[i][-1] == '5':
		print '%s: marco' % placas[i]
	elif placas[i][-1] == '6':
		print '%s: abril' % placas[i]
	elif placas[i][-1] == '7':
		print '%s: maio' % placas[i]
	elif placas[i][-1] == '8':
		print '%s: junho' % placas[i]
	elif placas[i][-1] == '9':
		print '%s: julho' % placas[i]
	elif placas[i][-1] == '0':
		print '%s: agosto' % placas[i]
