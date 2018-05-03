# coding: utf-8
# Unidade 4 - Lucro Mensal de uma Empresa
# Thaís Nicoly - UFCG 2015.2 - 11/03/2016

mes = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

saldo = []

for i in range(len(mes)):
	valor = raw_input().split()
	lucro = float(valor[0]) - float(valor[1])
	saldo.append(lucro)

for i in range(len(saldo)):
	if saldo[i] < 0:
		print '%s %.1f' % (mes[i],saldo[i])
	else:
		print '%s  %.1f' % (mes[i],saldo[i])
