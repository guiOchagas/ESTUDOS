"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

lista = []

qtd = int(input("Quantos números você quer? "))

for n in range(qtd):
    num = int(input(f"{n+1}º número: "))
    lista.append(num)

maior = (max(lista))
menor = (min(lista))
soma = maior + menor
print(f"Maior: {maior}\nMenor: {menor}\nSoma: {soma}")
