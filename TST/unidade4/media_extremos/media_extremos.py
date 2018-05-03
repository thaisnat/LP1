# coding: utf-8
# Unidade 4 - Classificação de Elementos Utilizando a Média dos Extremos
# Thaís Nicoly - UFCG 2015.2 - 14/03/2016

quantidade_n = int(raw_input())
numeros = []

if quantidade_n > 1:
# Receber os numeros e adicionar a uma lista
	for i in range(quantidade_n):
		numero = int(raw_input())
		numeros.append(numero)
		
	maior_numero = numeros[0]
	menor_numero = numeros[0]

# Comparando os valores que entram e substituindo caso seja verdadeira a condição 		
	for j in range(len(numeros)):
		if numeros[j] >= maior_numero:
			maior_numero = numeros[j]
		if numeros[j] <= menor_numero:
			menor_numero = numeros[j]
			
	print 'Menor número: %d' % menor_numero
	print 'Maior número: %d' % maior_numero
# Calculando a média
	media_extremos = (maior_numero + menor_numero)/ 2.0
	print 'Média dos extremos: %.2f' % media_extremos
		
	cont = 0
	soma = 0
# Separando os números que estão acima e abaixo da média
	for x in numeros:
		if x > media_extremos:
			cont += 1
		if x < media_extremos:
			soma +=1
	print '%d número(s) abaixo da média' % soma
	print '%d número(s) acima da média' % cont
		
		
