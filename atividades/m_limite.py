# coding: utf-8
# Unidade 5 - Média Atinge Limite
# Thaís Nicoly - UFCG 2015.1 - 13/11/2015

sequencia = []
soma,qnt = 0,0

while True:
	valores = raw_input()
	if valores == '--':
		break
	sequencia.append(valores)

limite = float(raw_input())

for i in range(len(sequencia)):
	soma += float(sequencia[i])
	qnt += 1
	media = soma / qnt
	
	if media > limite:
		print 'media = %.1f' % media
		print 'num = ',i+1
		break
