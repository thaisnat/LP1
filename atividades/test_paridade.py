#coding: utf-8

sequencia = raw_input()

verificacao = 0
for i in range(len(sequencia)-1):
	if sequencia[i] == '1':
		verificacao += 1
	
	if verificacao % 2 == 0 and sequencia[-1] == '1':
		print 'ERRO'
	if verificacao % 2 == 1 and sequencia[-1] == '0':
		print 'ERRO'	


'''
Paridade refere-se ao número de bits '1' de um determinado número binário. 
Na paridade par, quando o número de bits de valor '1' for ímpar, é adicionado um bit de valor '1' ao final da sequência, 
tornando o número de bits 1 par. 
Quando o número de bits de valor '1' é par, é adicionado um bit de valor '0' ao final da sequência. 
Este bit adicional chama-se de bit de paridade.'''

#Exemplos: Considere as sequências: 10, 1101, 11101, 0 e 1.
#Após o cálculo de paridade, teremos: 10(1), 1101(1), 11101(0), 0(0) e 1(1).
 
'''A paridade é utilizada para detectar erros nas transmissões, 
já que o seu cálculo é extremamente simples. Nos exemplos anteriores, 
seriam considerados erros de paridade se, para as sequências apresentadas, 
tivéssemos obtido os valores'''
# Ex: 10(0), 1101(0), 11101(1), 0(1) e 1(0)
