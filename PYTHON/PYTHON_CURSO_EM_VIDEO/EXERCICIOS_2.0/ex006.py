''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''

from random import randint
from time import sleep


ganhador = None
par = 'Par'
impar = 'Impar'
option_player = None
option_pc = None
vitorias = derrotas = 0

while True:
    pc = randint(1, 10)
    player = int(input('Par(2) ou Impar(1)?\n'))
    if player == 1:
        print(f'Você escolheu {impar}')
    else:
        print(f'Você escolheu {par}')

    print()
    jogada = int(input('Escolha sua jogada: '))
    
    for dot in range(3):
        sleep(0.5)
        print('.', end='', flush=True)
    
    if player == 1:
        option_player = impar
        option_pc = par
        result = pc + jogada
        if result % 2 == 1:
            ganhador = 'Player'
            vitorias += 1
        else:
            ganhador = 'PC'
            derrotas += 1
    
    if player == 2:
        option_player = par
        option_pc = impar
        option = par
        result = pc + jogada
        if result % 2 == 0:
            ganhador = 'Player'
            vitorias += 1
        else:
            ganhador = 'PC'
            derrotas += 1

    print()
    print(f'VOCÊ escolheu {option_player} e jogou {jogada}')
    sleep(1)
    print(f'PC escolheu {option_pc} e jogou {pc}')
    sleep(1)
    print(f'TOTAL: {(jogada + pc)}')
    sleep(1)
    print(f'GANHADOR: {ganhador}')
    print()
    print(f'VITORIAS: {vitorias}')
    print(f'DERROTAS: {derrotas}')
    print()

    continuar = str(input('CONTINUAR? [S/N]\n')).upper()
    if continuar == 'N':
        break
    else:
        pass

print('FIM DE JOGO, ATÉ A PRÓXIMA!')
