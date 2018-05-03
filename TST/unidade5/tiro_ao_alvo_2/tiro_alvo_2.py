# coding: utf-8
# Unidade 5 - Tiro ao Alvo 2
# Thaís Nicoly - UFCG 2015.2 - 07/04/2016
import math

distancias = []

while True:
	x = float(raw_input())
	y = float(raw_input())
	if x >= 200 or y >= 200: break
	distancia = math.sqrt(x**2 - y**2)
	distancias.append(distancia)

	
for i in range(len(distancias)):
	if distancias[i] < distancias[
