valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print()
print(f'O maior valor digitado foi: [{max(valores)}]\nO menor valor digitado foi: [{min(valores)}]')
print(f'O maior foi digitado nas posições: ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print()
print(f'O menor valor foi digitado nas posições: ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
print()
print()
valores2 = []
maior = menor = 0
for c in range(0, 5):
    valores2.append(int(input('Digita um valor: ')))
    if c == 0:
        maior = menor = valores2[c]
    else:
        if valores2[c] > maior:
            maior = valores2[c]
        if valores2[c] < menor:
            menor = valores2[c]
print()
print(f'O maior valor digitado foi: [{maior}]')
print(f'O menor valor digitado foi: [{menor}]')
print(f'O maior foi digitado nas posições: ', end='')
for i, c in enumerate(valores2):
    if c == maior:
        print(f'{i}... ', end='')
print()
print('O menor foi digitado nas posições: ', end='')
for i, c in enumerate(valores2):
    if c == menor:
        print(f'{i}... ', end='')
print()
