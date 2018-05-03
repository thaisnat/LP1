# coding: utf-8
# Unidade 4 - Quantos na Final?
# Thaís Nicoly - UFCG 2015.2 - 23/03/2015

q_estudantes = int(raw_input())

soma = 0
cont = 0
cont_m = 0

for i in range(q_estudantes):
	medias = float(raw_input())
	if medias < 7.0 and medias >= 4:
		cont += 1
		soma += medias
	else:
		cont_m += 1
		
if cont > 1:
	media = float(soma)/cont
	
perc_final = (cont * 100) / q_estudantes


if cont_m == q_estudantes:
	print '%d (%.1f%%) alunos na final' % (cont,(float(perc_final)))
else:
	print '%d (%.1f%%) alunos na final' % (cont,(float(perc_final)))
	print 'Média das notas: %.1f' % media
	
