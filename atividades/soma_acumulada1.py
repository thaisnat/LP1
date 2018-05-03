# coding: utf-8
# Unidade 4 - Exemplo de Programa de Soma Acumulada
# Thaís Nicoly - UFCG 2015.1 - 01/06/2015

n = int(raw_input())

soma_total = 0
for i in range(n):
	venda = float(raw_input())
	soma_total += venda

print soma_total

'''
Se não quiser que efetue a soma se caso o número for negativo
soma_total = 0
for i in range(n):
	venda = float(raw_input())
	if venda > 0:
	soma_total += venda

print soma_total '''
