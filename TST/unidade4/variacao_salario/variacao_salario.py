# coding: utf-8
# Unidade 4 - Análise de Variação do Salário Mínimo
# Thaís Nicoly - UFCG 2015.2 - 31/04/2015

ano_inicial = int(raw_input())
ano_final = int(raw_input())

maior = False
# ---
cont_total = 0
cont_maior = 0
cont_menor = 0
# ---
soma_maior = 0
soma_menor = 0

for i in range(ano_inicial,ano_final + 1):
	salario = float(raw_input())
	cont_total += 1
	if salario > 100.00:
		maior = True
	
	if maior:
		cont_maior += 1
		soma_maior += salario
	else:
		cont_menor += 1
		soma_menor += salario
		
perc_menor = (cont_menor * 100) / cont_total
perc_maior = 100 - perc_menor	

print '%d ano(s) abaixo (%d%% dos anos)' % (cont_menor,perc_menor)
if cont_menor >= 1:
	media_menor = soma_menor / cont_menor
	print 'média dos anos abaixo: U$ %.2f' % media_menor

print '%d ano(s) acima (%d%% dos anos)' % (cont_maior,perc_maior)
if cont_maior >= 1:
	media_maior = soma_maior / cont_maior
	print 'média dos anos acima: U$ %.2f' % media_maior
