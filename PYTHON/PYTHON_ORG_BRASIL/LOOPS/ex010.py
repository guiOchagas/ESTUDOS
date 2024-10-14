"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."""

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

while n1 < n2 - 1:
    n1 += 1
    print(n1)
