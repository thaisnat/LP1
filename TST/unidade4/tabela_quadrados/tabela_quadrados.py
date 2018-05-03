# coding: utf-8
# Unidade 4 - Tabela de Quadrados
# Thaís Nicoly - UFCG 2015.2 - 10/03/2016

x = int(raw_input())
y = int(raw_input())

if x > y:
    print '---'
else:
    for i in range (x,y+1):
        print i,i*i
