lista = [[], [], []]
dig = 0
for n in range(3):
    dig = int(input(f'Digite um valor para [0, {n}]: '))
    lista[0].append(dig)

for n in range(3):
    dig = int(input(f'Digite um valor para [1, {n}]: '))
    lista[1].append(dig)

for n in range(3):
    dig = int(input(f'Digite um valor para [2, {n}]: '))
    lista[2].append(dig)

for item in lista[0]:
    print(f'[ {item} ]', end='')
print()
for item in lista[1]:
    print(f'[ {item} ]', end='')
print()
for item in lista[2]:
    print(f'[ {item} ]', end='')
print()
