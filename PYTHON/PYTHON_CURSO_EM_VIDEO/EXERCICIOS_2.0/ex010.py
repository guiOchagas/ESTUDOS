'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense
'''

campeonato_brasileiro = (
    'Flamengo', 'Atlético-MG', 'Palmeiras', 'Fortaleza', 'Corinthians',
    'Bragantino', 'Fluminense', 'Internacional', 'Athletico-PR', 'Ceará',
    'São Paulo', 'Santos', 'América-MG', 'Atlético-GO', 'Juventude',
    'Cuiabá', 'Gremio', 'Bahia', 'Chapecoense', 'Sport'
)

# Os cinco primeiros colocados
for time in range(5):
    print(f'{time + 1}º - {campeonato_brasileiro[time]}')

# Os últimos 4 colocados
ultimos = len(campeonato_brasileiro)
index = ultimos - 4
print(campeonato_brasileiro[index:])

for time in campeonato_brasileiro[index::]:
    print(time)

# Os times ordenados
ordenados = list(campeonato_brasileiro)
ordenados.sort()
print('ORDEM ALFABÉTICA:')
for time in ordenados:
    print(time)

# Posicição de Chapecoense
print(f'A posição de Chapecoense é a {campeonato_brasileiro.index('Chapecoense')} na tabela.')
