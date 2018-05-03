# coding: utf-8
# Unidade 5 - Verifica Operações Extrato
# Thaís Nicoly - UFCG 2015.2 - 12/04/2016

limite_saques = int(raw_input())
saldo_atual = float(raw_input())

cont = 0

while True:
	operacao,valor = raw_input().split()
	
	if operacao == 'depósito':
		if float(valor) > 1000.00:
			print 'Operação inválida: depósito %.2f.' % float(valor)
			print 'Seu saldo é R$ %.2f.' % saldo_atual
			break 
		
		saldo_atual += float(valor)
	
	if operacao == 'saque':
		cont += 1
		saldo_atual = saldo_atual - float(valor)
		
		if cont > limite_saques:
			saldo_atual = saldo_atual + float(valor)
			print 'Operação inválida: saque %.2f.' % float(valor)
			print 'Seu saldo é R$ %.2f.' % saldo_atual
			break
			
		if saldo_atual < 0:
			saldo_atual = saldo_atual + float(valor)
			print 'Operação inválida: saque %.2f.' % float(valor)
			print 'Seu saldo é R$ %.2f.' % saldo_atual
			break
		
			
			
