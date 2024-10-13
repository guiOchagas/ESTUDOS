import random
print('='*20)
print('     JO-KEN-PÔ')
print('='*20)
print()
print('DIGITE UM NÚMERO PARA ESCOLHER A SUA JOGADA:')
print('1 | PEDRA\n2 | PAPEL\n3 | TESOURA')
print()

jogador = int(input(''))
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(jogadas)
print()
if jogador == 1:
    print('VOCÊ: *PEDRA*')
elif jogador == 2:
    print('VOCÊ: *PAPEL*')
elif jogador == 3:
    print('VOCÊ: *TESOURA*')
print()
if jogador == 1 or jogador == 2 or jogador == 3:
    print('COMPUTADOR: *{}*'.format(computador))
print()
if jogador == 1 and computador == 'PAPEL':
    print('VOCÊ PERDEU')
elif jogador == 1 and computador == 'PEDRA':
    print('EMPATE')
elif jogador == 1 and computador == 'TESOURA':
    print('VOCÊ GANHOU')
elif jogador == 2 and computador == 'PAPEL':
    print('EMPATE')
elif jogador == 2 and computador == 'PEDRA':
    print('VOCÊ GANHOU')
elif jogador == 2 and computador == 'TESOURA':
    print('VOCÊ PERDEU')
elif jogador == 3 and computador == 'PAPEL':
    print('VOCÊ GANHOU')
elif jogador == 3 and computador == 'PEDRA':
    print('VOCÊ PERDEU')
elif jogador == 3 and computador == 'TESOURA':
    print('EMPATE')
elif jogador > 3 or jogador == 0:
    print('OPÇÃO INVÁLIDA')
