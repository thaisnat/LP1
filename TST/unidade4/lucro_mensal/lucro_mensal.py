# coding: utf-8
# Unidade 4 - Lucro Mensal de uma Empresa
# Thaís Nicoly - UFCG 2015.2 - 23/03/2015

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

saldo = []

for i in range(len(meses)):
	valor = raw_input().split()
	lucro = float(valor[0]) - float(valor[1])
	saldo.append(lucro)

for i in range(len(saldo)):
	if saldo[i] < 0:
		print '%.1f' % saldo[i]
	else:
		print ' %.1f' % saldo[i]
