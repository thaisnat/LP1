# coding: utf-8
# unidade 4 -Tabela de Quadrados (Divisíveis por 3)
# Thaís Nicoly - UFCG 2015.2 - 30/03/2016

numeroX = int(raw_input())
numeroY = int(raw_input())

quadrados = []
numeros = []

if numeroX > numeroY:
    print '---'

for i in range(numeroX,(numeroY)+1):
    quadrado = i**2
    saida = '%d %d' % (i,quadrado)
    
    if quadrado % 3 == 0:
        saida += ' *'
    
    print saida
