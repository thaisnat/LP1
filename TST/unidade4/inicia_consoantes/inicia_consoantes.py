# coding: utf-8
# Unidade 4 - Iniciadas por consoantes
# Thaís Nicoly - UFCG 2015.2 - 22/03/2016

n = int(raw_input())

total = 0
inicia_consoante = 0

for i in range(n):
	palavra = raw_input()
	total += 1
	if palavra[0] not in 'AEIOUaeiou':
		inicia_consoante += 1

perc_consoantes = (float(inicia_consoante) * 100) / total

print 'total de palavras: %d' % total		
print 'iniciadas por consoantes: %d (%.2f%%)' % (inicia_consoante,perc_consoantes)
