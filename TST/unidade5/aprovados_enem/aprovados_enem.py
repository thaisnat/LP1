# coding: utf-8
# Unidade 5 - Aprovados no ENEM
# Thaís Nicoly - UFCG 2015.2 - 07/04/2016

candidatos = []
notas = []

while True:
	entrada = raw_input()
	if entrada == 'fim':
		break
	relatorio = entrada.split()
	candidatos.append(relatorio[0])
	notas.append(relatorio[1])
	
nota_de_corte = int(raw_input())
nao_foi_aprovado = True

for i in range(len(notas)):
	if int(notas[i]) >= nota_de_corte:
		nao_foi_aprovado = False
		print '%s, %s' % (candidatos[i],notas[i])

if nao_foi_aprovado:
	print 'Nenhum candidato aprovado.'
	
