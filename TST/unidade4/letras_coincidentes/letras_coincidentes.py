# coding: utf-8
# Unidade 4 - Letras Coincidentes
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

primeira_palavra = raw_input()
segunda_palavra = raw_input()
tamanho = 0
total = 0
posicao = []
coincidentes = []

# Saber qual a sequencia menor
if len(primeira_palavra) < len(segunda_palavra):
	tamanho = len(primeira_palavra)
else:
	tamanho = len(segunda_palavra)

for x in range(tamanho):
	if primeira_palavra[x] == segunda_palavra[x]:
		coincidentes.append(primeira_palavra[x])
		posicao.append(x+1)
		total +=1
		
tamanho_juntas = float(len(primeira_palavra)+len(segunda_palavra))
porcentagem = len(coincidentes)/tamanho_juntas*100

print 'Letras coincidentes' 
for i in range(len(posicao)): 
	print "'%s' na posição %s" % (coincidentes[i],posicao[i])
print 'Total de letras coincidentes: %d (%d%%)' % (total,porcentagem)
	
