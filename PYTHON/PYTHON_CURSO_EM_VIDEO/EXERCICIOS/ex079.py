lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Adicionado com sucesso!')
        print()
    else:
        print('Valor duplicado.')
        print()
    r = str(input('Continuar? [S/N] ')).upper()
    print()
    if r == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
