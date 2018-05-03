# coding: utf-8
# Unidade 4 - Ataque Mais Positivo de um Campeonato
# Thaís Nicoly - UFCG 2015.2 - 21/03/2016

n_times = int(raw_input())
times = []
gols = []

time_maior = ''
soma,maior = 0,0

for i in range(n_times):
	time = raw_input()
	gol = int(raw_input())
	
	times.append(time)
	gols.append(gol)
	
	soma += gol
	
	if gol > maior:
		maior = gol
		
print 'Time(s) com melhor ataque (%d gol(s)):'% maior 	
for x in range(n_times):
	if gols[x] == maior:
		print times[x]

print '\nMédia de gols marcados: %.1f' % (float(soma)/n_times)
