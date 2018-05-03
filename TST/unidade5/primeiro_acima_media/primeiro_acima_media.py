# coding: utf-8
# Unidade 5 - Primeiro Acima da Média
# Thaís Nicoly - UFCG 2015.2 - 11/04/2016

soma = 0
valores = []

while True:
	entrada = raw_input()
	if entrada == 'fim': break
	valores.append(entrada)
	
for i in range(len(valores)):
	soma += float(valores[i])
	
media = soma/float(len(valores))
	
for x in range(len(valores)):
	if float(valores[x]) > media:
		print '%d, %.2f > %.2f' % (x, float(valores[x]),media)
		break
