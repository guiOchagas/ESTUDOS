"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."""

lista = []

for n in range(10):
    num = int(input(f"{n+1}/10:"))
    lista.append(num)

print('PAR: ', end='')

for n in lista:
    if n % 2 == 0:
        print(n, end='')

print()

print('ÍMPAR: ',end='')
for n in lista:
    if n % 2 == 1:
        print(n, end='')
