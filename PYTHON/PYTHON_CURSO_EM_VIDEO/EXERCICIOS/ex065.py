go = 'S'
soma = cont = media = maior = menor = 0
while go in 'Ss':
    num = int(input('Digite um número: '))
    print()
    soma += num
    cont += 1
    media = soma / cont
    
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
            
    go = str(input('Deseja continuar? [S/N] ')).upper()
    print()
print()
print(f'Você digitou {cont} valores, a soma entre eles é {soma} e média é {media:.2f}.')
print()
print(f'O maior número é o {maior} e o menor é o {menor}')
print()
print('Até a próxima...')
