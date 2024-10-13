from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador_1': randint(1,9), 'jogador_2': randint(1,9), 'jogador_3': randint(1,9), 'jogador_4': randint(1,9)}
print('='*10)
print(f'   JOGO')
print('='*10)
for k, v in jogo.items():
    print(f'O {k} tirou [{v}]')
    sleep(1)

print()
print('='*10)
print(f' RESULTADO')
print('='*10)

ranking = {}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)


print()
