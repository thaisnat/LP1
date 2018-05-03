# coding: utf-8
# Unidade 5 - Pi por Aproximações (Questão do Miniteste)
# Thaís Nicoly - UFCG 2015.2 - realizado dia 08/04/2016

erro = float(raw_input())
denominador = 1
numerador = 1
soma = 0

while True:
	
	pi_anterior = 4 * soma
	soma += numerador / float(denominador)
	numerador += -1
	denominador += 2
	novo_pi = 4 * soma
	print '%.6f' % novo_pi
	if abs(novo_pi - pi_anterior) < erro: break
