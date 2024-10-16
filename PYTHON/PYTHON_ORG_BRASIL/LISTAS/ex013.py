"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""

from random import randint

mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temp = []

for t in range(12):
    temp.append(randint(6, 39))

media_temp = sum(temp) / len(temp)

for item in range(12):
    if temp[item] > media_temp:
        print(f"{mes[item]}: {temp[item]}")
    
print(temp)
print(f"{media_temp:.2f}")
