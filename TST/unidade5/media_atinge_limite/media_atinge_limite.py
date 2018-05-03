# coding: utf-8
# Unidade 5 - Média Atinge Limite
# Thaís Nicoly - UFCG 2015.2 - 14/04/2015

sequencia = []
soma,qnt = 0,0
tem = False

while True:
	valores = raw_input()
	if valores == '-':
		break
	sequencia.append(valores)

limite = float(raw_input())

for i in range(len(sequencia)):
	soma += float(sequencia[i])
	qnt += 1
	media = soma / qnt
	
	if media > limite:
		tem = False
		print 'media = %.1f' % media
		print 'num =',i+1
		break
	if media < limite:
		tem = True

if tem:		
	print 'limite não alcançado'
