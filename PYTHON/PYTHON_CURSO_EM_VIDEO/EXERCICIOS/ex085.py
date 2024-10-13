lista = [[], []]

for dig in range(4):
    numero = int(input(f'Digite o {dig+1}º número: '))
    if numero % 2 == 0:
        lista[0].append(numero)  # Adiciona números pares na primeira sublista
    else:
        lista[1].append(numero)  # Adiciona números ímpares na segunda sublista

print()
print(lista)
print()
print(f'PARES: {lista[0]}')
print()
print(f'ÍMPARES: {lista[1]}')
