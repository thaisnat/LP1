# coding: utf-8
# Unidade 2 - Quadrado inscrito em Circunferencia
# Thaís Nicoly - UFCG 2015.2 - 22/02/2016
import math

lado = float(raw_input())

diagonal = math.sqrt(lado**2 + lado**2)

raio = diagonal / 2

perimetro = math.pi*raio*2

area = math.pi*raio**2

print 'Perímetro: %.5f' % perimetro
print 'Área: %.5f' % area
