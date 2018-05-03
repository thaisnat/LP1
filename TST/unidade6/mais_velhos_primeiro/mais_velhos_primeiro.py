# coding: utf-8
# Unidade 6 - Mais Velhos Primeiro
# Thaís Nicoly - UFCG 2015.2 - 08/04/2016

def idosos_inicio(fila):
    primeiro = 0
    for i in range(len(fila)):
        primeiro_lista = fila[primeiro]
        if fila[i] >= 60:
            fila[i],fila[primeiro] = primeiro_lista,fila[i]
            primeiro += 1
                

