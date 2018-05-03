# coding: utf-8
# Unidade 4 - Vendas por mês (Questão do Miniteste)
# Thaís Nicoly - UFCG 2015.1 - 18/06/2015

quant = int(raw_input())
vendas = 12*[0]
soma = 0

for i in range(quant):
	registros = raw_input().split(',')
	soma += float(registros[1])
	vendas[int(registros[0])-1] += float(registros[1])

media = soma / quant

print media
for j in range(12):
	if vendas[j] >= media:
		print 'O mês %d vendeu bem.' % (j+1)
	
