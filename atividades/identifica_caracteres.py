# coding: utf-8
# Unidade 4 - Questão do Miniteste - Identifica Caracteres
# Thaís Nicoly - UFCG 2015.1 - 12/06/2015

p1 = raw_input()
p2 = raw_input()

resposta = ''
for letra in p2:
    indice = ''
    for i in range(len(p1)):
        if letra == p1[i]:
            indice += str(i) + ' '
            
    if indice == '':
        resposta += '-1 '
    else:
        resposta += indice 

print resposta
