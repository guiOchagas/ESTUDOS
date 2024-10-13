num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print()
print(f'{num} ')
print()
print(f'O valor [9] apareceu {num.count(9)} vez(es)')
print()
if 3 in num:
    print(f'O [3] apareceu na {num.index(3) + 1}º posição')
else:
    print(f'O valor [3] não foi digitado.')
print()
print(f'Os número pares digitas são: ')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')
