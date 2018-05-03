# coding: utf-8
# Unidade 4 - Sistema de Metas de Venda Mensal
# Thaís Nicoly - UFCG 2015.2 - 28/03/2016

meta_mes = float(raw_input())

meta_individual = meta_mes/6
vendas = []
saldo = 0
meta_ok = True

for i in range(6):
	venda = float(raw_input())
	vendas.append(venda)
	saldo += venda
	
	if venda < meta_individual:
		meta_ok = False
		
if meta_ok and saldo >= meta_mes:
	print 'Total de vendas: R$ %.2f (meta atingida)\n----\nBonificação:' % saldo
	
	for i in range(len(vendas)):
		bon = vendas[i] * 0.01
		print 'Funcionário %d: R$ %.2f' % (i+1, bon)
else:
	print 'Total de vendas: R$ %.2f (meta não foi atingida)\n----' % saldo
