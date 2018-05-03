# coding: utf-8
# unidade 4 - Divisores Próprios
# Thaís Nicoly - UFCG 2015.2 - 30/03/2016

num = int(raw_input())

for i in range(1,num):
    if num % i == 0:
        print i
    
