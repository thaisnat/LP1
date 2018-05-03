# coding: utf-8
# Unidade 4 - Utilizando o Teorema de Herão para Calcular a Área de Triângulos
# Thaís Nicoly - UFCG 2015.2 - 21/03/2016

import math
q_triangulos = int(raw_input())
areas = [] 

for i in range(q_triangulos):
	lados = raw_input().split()
	area = 0
	for x in range(len(lados)):
		soma_lados = float(lados[0]) + float(lados[1]) + float(lados[2])
		s = soma_lados / 2
		sa = s - float(lados[0])
		sb = s - float(lados[1])
		sc = s - float(lados[2])
		area = math.sqrt(s*sa*sb*sc)
		
	areas.append(area)
		
cont = 0
soma_areas = 0

for j in range(len(areas)):
	print 'Área %d: %.2f' % (j+1,areas[j])
	if areas[j] > 100:
		cont += 1
		soma_areas += areas[j]
		
media_areas = soma_areas / cont
		
print 'Número maiores: %d, área média: %.2f' % (cont,media_areas)		
		
