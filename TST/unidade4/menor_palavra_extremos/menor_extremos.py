# coding: utf-8
# Unidade 4 - Menor Palavra dos Extremos
# Thaís Nicoly - UFCG 2015.2 - 18/03/2016

n = int(raw_input())

palavras = []

for i in range(n):
	palavra = raw_input()
	palavras.append(palavra)

primeira = palavras[0]
ultima = palavras[-1]

menores = []

if len(primeira) > len(ultima):
	menores.append(ultima)
elif len(primeira) < len(ultima):
	menores.append(primeira)
else:
	menores.append(primeira)
	menores.append(ultima)

qt_maiores = 0
qt_menores = 0

for i in range(len(palavras)):
	if len(palavras[i]) < len(menores[0]):
		qt_menores +=1
	elif len(palavras[i]) > len(menores[0]):
		qt_maiores +=1

if len(menores) > 1:
	print 'Menor palavra dos extremos: %s, %s (%d letras)' % (menores[0],menores[1], len(menores[0]))
else:
	print 'Menor palavra dos extremos: %s (%d letras)' % (menores[0],len(menores[0]))
	
print '%d palavra(s) com tamanho menor' % qt_menores
print '%d palavra(s) com tamanho maior' % qt_maiores
