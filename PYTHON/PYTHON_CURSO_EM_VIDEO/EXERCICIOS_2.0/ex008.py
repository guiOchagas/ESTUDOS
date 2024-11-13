'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''

soma = 0
caro = 0
nome_caro = None
barato = 0
nome_barato = None

while True:
    produto = str(input('PRODUTO: '))
    preco = float(input('PREÇO: '))
    print()

    #Total da compra
    soma += preco

    #Produto mais caro
    if preco > caro:
        caro = preco
        nome_caro = produto

    #Produto mais barato
    if barato == 0 or preco < barato:
        barato = preco
        nome_barato = produto

    #Validação para continuar com o programa
    while True:
        keep = str(input('Continuar? [S/N] ')).upper()
        print()
        if keep == 'S':
            break
        elif keep == 'N':
            break
        else:
            print('Erro')

    if keep == 'N':
        break

print(f'TOTAL GASTO: R${soma:.2f}')
print(f'PRODUTO MAIS CARO: {nome_caro} = R${caro:.2f}')
print(f'PRODUTO MAIS BARATO: {nome_barato} = R${barato:.2f}')
