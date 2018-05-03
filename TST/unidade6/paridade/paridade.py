# coding: utf-8
# Unidade 6 - Paridade
# Thaís Nicoly - UFCG 2015.2 - 07/04/2016

def paridade(sequencia):
		verificacao = 0
		for i in range(len(sequencia)-1):
			if sequencia[i] == '1':
				verificacao += 1
			
		if verificacao % 2 == 0 and sequencia[-1] == '1':
			return 'ERRO'
		if verificacao % 2 == 1 and sequencia[-1] == '0':
			return 'ERRO'
while True:
	sequencia = raw_input()
	if paridade(sequencia): 
		print paridade(sequencia)
		break
