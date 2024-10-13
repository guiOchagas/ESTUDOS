def ficha(nome='<desconhecido>', gols=0):
    print(f'O {nome} fez {gols} gol(s) no campeonato.')

jogador = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)
