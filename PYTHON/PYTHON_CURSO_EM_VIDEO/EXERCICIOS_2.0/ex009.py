'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

from time import sleep

saque = int(input('Insira o valor de saque: '))
saque_total = saque
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_1 = 0

print()
print(f'Valor a ser sacado: [R${saque_total}]')

while True:
    while saque >= 50:
        saque -= 50
        nota_50 += 1
        if saque < 50:
            break

    while saque >= 20:
        saque -= 20
        nota_20 += 1
        if saque < 20:
            break

    while saque >= 10:
        saque -= 10
        nota_10 += 1
        if saque < 10:
            break

    while saque >= 1:
        saque -= 1
        nota_1 += 1
        if saque < 1:
            break
        
    break

print(f'Processando saque...')
sleep(1)
print()
print('Saque realizado:')
sleep(1)
print(f'TOTAL: {saque_total}')
sleep(1)
print(f'Separação das notas:\nR$50: {nota_50}\nR$20: {nota_20}\nR$10: {nota_10}\nR$1: {nota_1}')
