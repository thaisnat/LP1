# coding: utf-8
# Unidade 4 - Percentual de Alunos Aprovados
# Thaís Nicoly - UFCG 2015.2 - 23/03/2015

alunos = int(raw_input())
aprovados = 0
medias = []

for i in range(alunos):
	media = raw_input()
	medias.append(media)
	
for x in range(len(medias)):
	if medias[x] != 'F':
		if float(medias[x]) >= 5.0:
			aprovados += 1
			print aprovados
		
perc_aprov = (aprovados * 100) / alunos
	

print 'd% (%d/%d) de aprovados' % (perc_aprov,aprovados,alunos)
