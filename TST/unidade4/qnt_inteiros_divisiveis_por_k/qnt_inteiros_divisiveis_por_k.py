# coding: utf-8
# Unidade 4 - Quantidade de Inteiros Divisíveis por K
# Thaís Nicoly - UFCG 2015.2 - 10/03/2016

cont = 0
perc = 0
valores = []

numero_k = int(raw_input())
n = int(raw_input())

for i in range(n):
	sequencia = int(raw_input())
	valores.append(sequencia)
	
for x in range(len(valores)):
	if valores[x] % numero_k == 0:
		cont += 1
		
perc = ((float(cont)) / len(valores))*100

print '%d (%.1f%%)' % (cont,perc)

