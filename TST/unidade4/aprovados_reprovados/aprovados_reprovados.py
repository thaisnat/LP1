# coding: utf-8
# Unidade 4 - Aprovados e Reprovados
# Thaís Nicoly - UFCG 2015.2 - 28/03/2016

q_alunos = int(raw_input())

q_aprovados,soma_aprovados = 0,0
q_reprovados,soma_reprovados = 0,0

for i in range(q_alunos):
	nota = float(raw_input())
	
	if nota >= 7:
		soma_aprovados += nota
		q_aprovados += 1
	else:
		soma_reprovados += nota
		q_reprovados += 1
		
media_aprovados, media_reprovados = 0,0

if q_reprovados == 0:
	print 'Reprovados: %d\n' % q_reprovados
else:
	print 'Reprovados: %d' % q_reprovados
if q_reprovados >= 1:
	media_reprovados = soma_reprovados / q_reprovados
	print 'Média: %.1f\n' % media_reprovados
	
print 'Aprovados: %d' % q_aprovados
if q_aprovados >= 1:
	media_aprovados = soma_aprovados / q_aprovados
	print 'Média: %.1f' % media_aprovados
