"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

pais_a = 80000
taxa_a = 0.03

pais_b = 200000
taxa_b = 0.015

cont = 0

while pais_a <= pais_b:
    pais_a += pais_a * taxa_a
    pais_b += pais_b * taxa_b
    cont += 1

print(f'Serão {cont} anos necessários para que o país A ultrapasse o país B é. No final a população do país A será de {pais_a} e do país B será de {pais_b}.')
