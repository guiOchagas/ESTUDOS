lista = []
maior = menor = 0

for c in range(5):
    n = int(input(f'Digite o {c+1}º número: '))
    lista.append(n)
    if c == 0:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'Você digitou os valores {lista}')

print(f'O maior valor foi {maior} e estão nas posições: ')

for i, v in enumerate(lista):
    if v == maior:
        print(i + 1)

print(f'O menor valor foi {menor} e estão nas posições: ')

for i, v in enumerate(lista):
    if v == menor:
        print(i + 1)
