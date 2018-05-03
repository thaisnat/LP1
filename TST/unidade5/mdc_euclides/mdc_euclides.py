# coding: utf-8
# Unidade 5 - MDC por Euclides
# Thaís Nicoly - UFCG 2015.2 - 07/04/2016

numero_m = int(raw_input())
numero_n = int(raw_input())

while numero_n != 0:
    resto = numero_m % numero_n
    numero_m = numero_n
    numero_n = resto

print numero_m
