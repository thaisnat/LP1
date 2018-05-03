# coding: utf-8
# Unidade 5 - Limite Acima Criminalidade ( Questão do Miniteste)
# Thaís Nicoly - UFCG 2015.1 - 23/10/2015

media_limite = float(raw_input())
relatorio = []

while True:
   entrada = raw_input()
   if entrada == 'fim' : break
   tokens = entrada.split()
   
   # Calculo da média
   soma = 0
   
   for i in range(len(tokens)):
	   soma += int(tokens[i])
   media = float(soma/len(tokens))
   
   if media < media_limite / 2:
	   break
   if media > media_limite:
	   relatorio.append(entrada)

for linha in relatorio:
	print linha
