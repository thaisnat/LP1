# coding: utf-8
# Unidade 2 - Percentual de Reajuste
# Thaís Nicoly - UFCG 2015.2 - 22/02/2016

salario = float(raw_input())
novo_salario = float(raw_input())

aumento = novo_salario - salario
perc_aumento = (aumento/salario) * 100

print 'Valor atual? Novo valor? Reajuste de %.1f%%' % perc_aumento
