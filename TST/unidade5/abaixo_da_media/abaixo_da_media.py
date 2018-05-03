# coding: utf-8
# Unidade 5 - Abaixo da Média
# Thaís Nicoly - UFCG 2015.2 - 10/03/2016

soma = 0
media = 0
sequencia_numeros = []

while True:
	sequencia = raw_input()
	if sequencia == 'fim':
		break
	soma += int(sequencia)
	sequencia_numeros.append(sequencia)

#calculo da média
media = float(soma) / len(sequencia_numeros)

print '%.2f' % media

# descobrir quais valores são menores que a média	
for i in range(len(sequencia_numeros)):
	if int(sequencia_numeros[i]) < media:
		print i+1,sequencia_numeros[i]
	
	


'''A primeira linha da saída deve conter o valor da média, 
com duas casas decimais. 
Nas demais linhas devem ser impressas apenas os valores menores que a média dos valores lidos 
e a respectiva posição que o valor ocupa na sequência. 
Por exemplo, se o primeiro valor da sequência for 10 e for menor que a média, 
deverá ser impresso o valor "1 10" na saída.
'''
