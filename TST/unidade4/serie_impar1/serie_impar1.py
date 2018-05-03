# coding: utf-8
# Unidade 4 - Série Impar I
# Thaís Nicoly - UFCG 2015.2 - 28/03/2015

for i in range (1, 102, 2):
    if i % 3 == 0 or i % 5 == 0:
        print '*'
    else:
        print i
