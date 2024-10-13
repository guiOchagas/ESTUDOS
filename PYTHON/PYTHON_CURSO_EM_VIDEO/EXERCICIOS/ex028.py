from random import randint
from time import sleep
computador = randint(0,5)
print('Oi, sou o seu computador')
sleep(1)
print('Eu duvido você advinhar em que número estou pensando!')
sleep(1)
print('')
print('Tenta a sorte, escolha um número de 1 a 5: ')
print('')
jogador = int(input(''))
print('')
if jogador == computador:
    print('CARACA, COMO VOCê SABIA???')
else:
    print('ERROUUUUU, HEHEHEH')
