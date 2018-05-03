# coding: utf-8
# Unidade 5 - Reprovado por Faltas ( Questão do Miniteste)
# Thaís Nicoly - UFCG 2015.1 - 23/10/2015

reprovados = 0

while True:
	registro = raw_input()
	if registro == '-': break
	indice = 0
	faltas = 0
	while faltas <= 8 and indice < len(registro):
		if registro[indice] == 'f':
			faltas += 1
			indice += 1
		if faltas > 8:
			reprovados += 1
print reprovados
