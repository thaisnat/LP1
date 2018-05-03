# coding: utf-8
# Unidade 3 - Pedágio
# Thaís Nicoly - UFCG 2015.2 - 29/02/2016

veiculo = raw_input()

if veiculo == 'Automóveis Utilitários':
	eixos = int(raw_input())
	valor = eixos * 11.40
	print 'Valor a pagar: R$ %.2f.' % valor
elif veiculo == 'ônibus':
	eixos = int(raw_input())
	valor = eixos * 11.40
	print 'Valor a pagar: R$ %.2f.' % valor
elif  veiculo == 'Caminhão':
	eixos = int(raw_input())
	valor = eixos * 9.60
	print 'Valor a pagar: R$ %.2f.' % valor
elif veiculo == 'Motocicleta':
	eixos = int(raw_input())
	valor = eixos * 5.70
	print 'Valor a pagar: R$ %.2f.' % valor
else:
	print 'Veículo não cadastrado.'
