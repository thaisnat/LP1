# coding: utf-8
# Unidade 7 - Calculadora
# Thaís Nicoly - UFCG 2015.2 - 28/04/2016

def adicao(valor1,valor2):
	return valor1 + valor2

def subtracao(valor1,valor2):
	return valor1 - valor2

def multiplicacao(valor1,valor2):
	return valor1 * valor2

def divisao(valor1,valor2):
	if valor2 == 0:
		return 'Erro: Divisão por 0'
	else:
		return valor1 / valor2
		
while True:
	entrada = raw_input()
	if entrada == '5': break
	codigo,valor1,valor2 = entrada.split()
	
	if codigo == '1':
		print adicao(int(valor1),int(valor2))
	elif codigo == '2':
		print subtracao(int(valor1),int(valor2))
	elif codigo == '3':
		print multiplicacao(int(valor1),int(valor2))
	elif codigo == '4':
		print divisao(int(valor1),int(valor2))
