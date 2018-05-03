# coding: utf-8
# Unidade 5 - Operações Bancárias
# Thaís Nicoly - UFCG 2015.2 - 14/04/2015

dados = raw_input().split()
saldo = float(dados[1])

while True:
	entrada = raw_input().split()
	if entrada[0] == '1':
		saldo -= float(entrada[1])
	elif entrada[0] == '2':
		saldo += float(entrada[1])
	else:
		entrada[0] == '3'
		break

print 'Saldo de R$ %.2f na conta de %s' % (saldo,dados[0])
