from time import sleep
print('Quer saber se o número é PAR ou ÍMPAR?')
print('=' * 39)
n = int(input('Digite qualquer número: '))
validador = n % 2
print()
print('PROCESSANDO...')
print()
sleep(2)
if validador == 1:
    print('O número que você digitou é ÍMPAR')
else:
    print('O número que você digitou é PAR')
