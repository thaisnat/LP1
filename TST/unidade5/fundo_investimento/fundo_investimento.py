# coding: utf-8
# Unidade 5 - Fundo de Investimento
# Thaís Nicoly - UFCG 2015.2 - 14/04/2015

soma,qnt,media,quantia = 0,0,0,0

while True:
	if quantia < media:
		soma -= quantia
		qnt -= 1
		media = soma/ qnt
		break
	quantia = float(raw_input())
	soma += quantia
	qnt += 1
	media = soma / qnt
	

print 'Saldo total do FIS: R$%.2f.' % soma
print 'Média das contribuições: R$%.2f.' % media
