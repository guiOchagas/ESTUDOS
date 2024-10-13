from random import randint
print('='*30)
print('{:^30}'.format('JOGO DA ADIVINHAÇÃO'))
print('='*30)
print()
print('Pensei em um número de 0 à 5, tenta a sorte.')
print()

computador = randint(0, 5)
print(computador)
print()

acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    print()
    tentativas += +1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tenta um número mais alto!')
        else:
            print('Tenta um número menor')
print()
print('ACERTOU!')
print()
print(f'Você tentou {tentativas} tentativas.')
