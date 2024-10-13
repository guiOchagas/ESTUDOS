futebol = {}
futebol['nome'] = str(input('Nome do jogador: '))
print()

partidas = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))
print()

futebol['gols'] = []
total_gols = 0

for c in range(1, partidas + 1):
    futebol['gols'].append(int(input(f'Quantos gols na {c}º partida? ')))
    
for i in futebol['gols']:
    total_gols += i

futebol['total'] = total_gols

print()
print(futebol)
print()

for k, v in futebol.items():
    print(f'O {k} tem o valor {v}.')

print()
print('='*20)
print()

print(f'O jogador {futebol["nome"]} jogou {partidas} partidas.')

for c in range(partidas):
    print(f'  => Na partida {c + 1}, fez {futebol["gols"][c]}.')
