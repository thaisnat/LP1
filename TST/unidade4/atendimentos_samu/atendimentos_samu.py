# coding: utf-8
# Unidade 4 - Atendimentos no samu
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

soma = 0
n_atendimentos = []

for i in range(12):
	atendimentos = int(raw_input())
	soma += atendimentos
	n_atendimentos.append(atendimentos)

media = soma / 12.0
print 'Média mensal de atendimentos: %.2f' % media
print '----'

for i in range(len(n_atendimentos)):
	if n_atendimentos[i] > media:
		print 'Mês %d: %d' % (i+1,n_atendimentos[i])
