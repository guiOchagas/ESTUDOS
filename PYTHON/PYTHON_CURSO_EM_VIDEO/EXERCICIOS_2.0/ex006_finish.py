''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''

from random import randint

vitorias = 0
ganhador = None
par = impar = None

while True:
    pc = randint(1, 10)
    
    player = int(input('Par(2) ou Impar(1)? '))
    
    print()
    jogada = int(input('Escolha sua jogada: '))
    
    print('...')
    
    if player == 1:
        result = pc + jogada
        if result % 2 == 1:
            ganhador = 'Player'
        else:
            ganhador = 'PC'
    
    if player == 2:
        result = pc + jogada
        if result % 2 == 0:
            ganhador = 'Player'
        else:
            ganhador = 'PC'
            
    
    print(f'PLAYER: {jogada}\nPC: {pc}\nTOTAL: {(jogada + pc)}\nGANHADOR: {ganhador}')
