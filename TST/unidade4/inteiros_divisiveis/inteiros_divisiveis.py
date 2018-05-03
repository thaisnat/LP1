# coding: utf-8
# unidade 4 - Inteiros Positivos Divisiveis
# Thaís Nicoly - UFCG 2015.2 - 30/03/2016

numeroA = int(raw_input())
numeroB = int(raw_input())
numeroK = int(raw_input())

for i in range(1,(numeroK)+1):
    if i % numeroA == 0 and i % numeroB == 0:
        print i 
