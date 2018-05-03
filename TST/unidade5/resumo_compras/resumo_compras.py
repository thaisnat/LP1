# coding: utf-8
# Unidade 5 - Resumo Compras
# Thaís Nicoly - UFCG 2015.2 - 11/04/2016

soma,quant,maior = 0,0,0

while True:
	entrada = raw_input()
	if entrada == 'fim': break
	
	soma += float(entrada)
	quant += 1
	
	if float(entrada) > maior:
		maior = float(entrada)

media = soma/quant

print 'O valor médio por produto foi R$ %.2f. O produto mais caro custa R$ %.2f.' % (media,maior)
