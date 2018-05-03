# coding: utf-8
# Unidade 5 - Aula de médias
# Thaís Nicoly - UFCG 2015.2 - 14/04/2015

num = []
soma = 0

while True:
	numeros = float(raw_input())
	soma += numeros
	num.append(numeros)
	
	if soma >= 100:
		break

media = soma/len(num)

print '''Quantidade de números lidos: %d
Soma dos números lidos: %.2f
Média = %.2f''' % (len(num),soma,media)

print 
print 'Abaixo da média'
for i in range(len(num)):
	if num[i] < media:
		print '%.2f (%do)' % (num[i],i+1)
		
print 
print 'Acima da média'
for i in range(len(num)):
	if num[i] > media:
		print '%.2f (%do)' % (num[i],i+1)
		
