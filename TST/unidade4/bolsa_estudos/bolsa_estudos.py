# coding: utf-8
# Unidade 4 - Economizando a Bolsa de Estudos
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

valor = []
maior,reserva = 0,0
bolsa = 500
mes = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

for i in range(len(mes)):
	despesa = int(raw_input())
	reserva += bolsa - despesa
	valor.append(reserva)
	if valor[i] >= valor[maior]:
		maior = i
		
print mes[maior]
