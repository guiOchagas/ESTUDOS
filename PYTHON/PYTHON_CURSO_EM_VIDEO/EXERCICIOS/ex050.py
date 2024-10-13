soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print()
print('Você digitou {} números PARES e a soma deles é {}'.format(cont, soma))
