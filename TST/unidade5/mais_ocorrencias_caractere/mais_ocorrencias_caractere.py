# coding: utf-8
# Unidade 5 - Mais Ocorrências de um Caractere
# Thaís Nicoly - UFCG 2015.2 - 14/04/2015

seq_palavras = []
quant = []
tem = 0

while True:
	palavra = raw_input()
	if palavra == 'fim': break
	seq_palavras.append(palavra)

caractere = raw_input()
inteiro_dado = int(raw_input())

for i in range(len(seq_palavras)):
	for j in range(len(seq_palavras[i])):
		if seq_palavras[i][j] == caractere:
			tem += 1
	quant.append(tem)
	if tem == 0:
		quant.append(tem)
		
print quant	
for x in range(len(quant)-1):
	if quant[x] > inteiro_dado:
		print seq_palavras[x]
