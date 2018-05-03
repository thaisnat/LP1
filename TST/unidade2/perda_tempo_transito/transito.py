# coding: utf-8
# Unidade 2 - Perda de Tempo no Trânsito
# Thaís Nicoly - UFCG 2015.2 - 22/02/2016

seg = int(raw_input())
ter = int(raw_input())
qua = int(raw_input())
qui = int(raw_input())
sex = int(raw_input())

soma = seg + ter + qua + qui + sex
media = soma / 5
perc_tempo = float(soma) / 72
episodios = soma / 50

print 'Você perdeu %d min na semana (média de %.2f min por dia).' % (soma,media)
print 'Isso significa %.2f%% da sua semana produtiva.' % perc_tempo
print 'Daria para assistir %d episódio(s) de House.' % episodios
