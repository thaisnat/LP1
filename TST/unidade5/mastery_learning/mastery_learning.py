# coding: utf-8
# Unidade 5 - Mastery Learning
# Thaís Nicoly - UFCG 2015.2 - 11/04/2016

print 'Mastery Learning'
print 'Cálculo da nota na unidade'
print 
nota1 = float(raw_input('Nota? '))
nota2 = float(raw_input('Nota? '))

if nota1 <= nota2:
	menor = nota1
	maior = nota2
else:
	menor = nota2
	maior = nota1

media_parcial = (nota1 + nota2)/2	
penalizacao = 0.0

while True:
	if media_parcial >= 6.0:
		print 'Média: %.1f (aprovado)' % media_parcial
		print 'Penalização: %.1f' % penalizacao
		break
	else:
		print 'Média: %.1f (cursando)' % media_parcial
		print 'Penalização: %.1f' % penalizacao
		print
		nova_nota = float(raw_input('Nota? '))
		penalizacao += 0.5
		
		if nova_nota > menor:
			menor = nova_nota
			if menor > maior:
				x = maior
				maior = menor
				menor = x
			else:
				x = menor
				menor = maior
				maior = x
				
			media_parcial = (menor + maior) / 2
print 
print '==='
print 'Notas válidas: %.1f e %.1f' % (maior,menor)
print 'Média parcial na unidade: %.1f' % media_parcial
print 'Penalizações: %.1f' % penalizacao
print 'Média final na unidade: %.1f' % (media_parcial-penalizacao)
