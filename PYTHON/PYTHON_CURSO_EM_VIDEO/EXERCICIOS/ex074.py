from random import randint
tupla = (randint(0, 9), randint(0, 9), randint(0, 10), randint(0, 9), randint(0, 9), )
ext = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez','onze','doze','treze','quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito')
for c in tupla:
    print(f'{c}', end=' ')
print()
print(f'Maior: [{max(tupla)}]')
print(f'Menor: [{min(tupla)}]')
print(f'E a soma entre eles é [{max(tupla)+min(tupla)}]')
soma = max(tupla) + min(tupla)
print()
print(f'Esse número por escrito é: [{ext[soma - 1]}]')
