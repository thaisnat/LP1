# coding: utf-8
# Unidade 2 - Calcula o preço de venda
# Thaís Nicoly - UFCG 2015.2 - 22/02/2016


entrada = float(raw_input())
despesas = float(raw_input())
lucro_desejado = float(raw_input())
perc_impostos = float(raw_input())
perc_comissoes = float(raw_input())
perc_descontos = float(raw_input())
perc_encargos = float(raw_input())

perc_despesas = (despesas/100) * entrada
perc_lucro = (lucro_desejado/100) * entrada

val1 = (entrada + perc_despesas + perc_lucro) * 100
val2 = (100 - perc_impostos - perc_comissoes - perc_descontos - perc_encargos)

preco_venda = val1/val2

print 'Preço de venda é R$ %.2f (R$ %.2f + R$ %.2f)' % (preco_venda,int(preco_venda),preco_venda-int(preco_venda))
