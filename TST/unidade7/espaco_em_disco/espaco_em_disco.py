# coding: utf-8
# Unidade 7 - Espaço em Disco
# Thaís Nicoly - UFCG 2015.2 - 20/04/2016

soma = 0
while True:
	entrada = raw_input()
	if entrada == 'fim': break
	login,espaco_disco = entrada.split()
	soma += float(espaco_disco)
	
'''
Pelo menos duas funções devem ser criadas: 
uma para realizar a conversão do espaço ocupado em disco de bytes para megabytes
 e uma outra para calcular o percentual de uso. '''

# 1 megaByte (Mb) = 1 024 kb = 1 048 576 Bytes

def converte_valores(espaco_disco):
	megaByte = 1048576
	novo_valor = float(espaco_disco) / megaByte
	
	return novo_valor

def percentual_uso_espaco_disco(valor):
	perc = (converte_valores(valor) * 100) / soma
	
	return perc

'''
SPLab - Espaço utilizado pelos usuários
---------------------------------------------
Nr., Usuário, Espaço Utilizado, % do uso
'''
for x in range(len(login)):
	valor = converte_valores(float(espaco_disco[x]))
	perc = percentual_uso_espaco_disco(valor)
	print '%d, %s, %.2f MB, %.2f%%' % (x+1,login[x],valor,perc)
	
'''
1, abrantes, 118.24 MB, 27.36%
2, dalton, 94.19 MB, 21.80%
3, eliane, 41.54 MB, 9.61%
4, wilkerson, 94.08 MB, 21.77%
5, massoni, 82.97 MB, 19.20%
6, martha, 0.12 MB, 0.03%
7, uian, 1.00 MB, 0.23%
Espaço total ocupado: 432.15 MB
Espaço médio ocupado: 61.74 MB

'''
