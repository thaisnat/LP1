# coding: utf-8
# Unidade 4 - Percentual de Alunos Aprovados
# Thaís Nicoly - UFCG 2015.2 - 28/03/2016

q_alunos = int(raw_input())

medias = []
aprovados = 0 

for i in range(q_alunos):
	media = raw_input()
	medias.append(media)

for i in range(len(medias)):
	if medias[i] != 'F':
		if float(medias[i]) >= 5.0:
			aprovados += 1

perc_alunos_aprovados = ((aprovados*100)/q_alunos)

print '%d%% (%d/%d) de aprovados' % (perc_alunos_aprovados,aprovados,q_alunos)
