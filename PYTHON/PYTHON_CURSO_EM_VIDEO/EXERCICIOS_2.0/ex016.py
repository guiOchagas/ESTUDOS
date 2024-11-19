"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""
dicio = {}


jogador = str(input('NOME: '))
partidas = int(input('JOGOU QUANTAS PARTIDAS? '))

dicio['JOGADOR'] = jogador
dicio['PARTIDAS'] = partidas
dicio['GOLS'] = list()

for x in range(partidas):
    gol = int(input(f'{x + 1}º partida: '))
    dicio['GOLS'].append(gol)

dicio['TOTAL_DE_GOLS'] = sum(dicio['GOLS'])

print(dicio)

print(f'O jogador {dicio["JOGADOR"]} jogou {dicio["PARTIDAS"]} partidas')

print('Tabela de pontos:')
for i, gol in enumerate(dicio['GOLS']):
    print(f'No {i + 1}º jogo fez: {gol} gol(s)')

print(f'Totalizando {dicio["TOTAL_DE_GOLS"]} gol(s) no campeonato!')
