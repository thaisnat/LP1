# coding: utf-8
# Unidade 6 - Retorna Maior e Menor Número
# Thaís Nicoly - UFCG 2015.2 - 25/04/2016

def retorna_maior_menor(numeros):
	saida = []
	maior = numeros[0]
	menor = numeros[0]
	for i in range(1,len(numeros)):
		if numeros[i] < menor:
			menor = numeros[i]
		if numeros[i] > maior:
			maior = numeros[i]
	saida.append(maior)
	saida.append(menor)
	
	return saida
