#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = 0

while True:
    try:
        nota = int(input('Digite um número: '))
        print(f'Você digitou o número {nota}')
        break
    except:
        print('Você digitou um valor inválido, por favor digite um número inteiro.')
