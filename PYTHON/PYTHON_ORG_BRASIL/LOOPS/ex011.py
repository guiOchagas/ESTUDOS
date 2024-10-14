"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."""

"""Altere o programa anterior para mostrar no final a soma dos números.
"""

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
soma = 0

while n1 < n2 - 1:
    n1 += 1
    print(n1)
    soma += n1

print(soma)
