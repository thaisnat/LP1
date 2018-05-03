# coding: utf-8
# Unidade 5 - Conversão de R$ para Dólar, Peso e Euro
# Thaís Nicoly - UFCG 2015.2 - 04/04/2016

# declaração dos simbolos
simbolo_dolar = 'U$'
simbolo_peso = '$'
simbolo_euro = '€'

# conversão dos valores 
real = 1.00
dolar = 0.49
peso = 2.58
euro = 0.38

saida = []
valores = []
simbolo_valor = []

while True:
	entrada = raw_input()
	if entrada == 'fim' : break
	entrada_acessada = entrada.split()
	
	if entrada_acessada[-1] == simbolo_dolar:
		converte_dolar = dolar*(float(entrada_acessada[1]))/ real
		saida.append(converte_dolar)
	elif entrada_acessada[-1] == simbolo_peso:
		converte_peso = peso*(float(entrada_acessada[1]))/ real
		saida.append(converte_peso)
	elif entrada_acessada[-1] == simbolo_euro:
		converte_euro = euro*(float(entrada_acessada[1]))/ real
		saida.append(converte_euro)
	simbolo_valor.append(entrada_acessada[-1])
	valores.append(entrada_acessada[1])
		
for i in range(len(saida)):
	print 'R$ %s = %s %.2f' % (valores[i],simbolo_valor[i],saida[i])
		
		
	
