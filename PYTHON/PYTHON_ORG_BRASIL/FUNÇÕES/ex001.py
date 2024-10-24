"""Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha."""


def piramide(num):
    for valor in range(1, num + 1):
        for outro in range(valor):
            print(valor, end='   ')
        print()
            
digite = int(input('Digite um valor: '))
piramide(digite)
