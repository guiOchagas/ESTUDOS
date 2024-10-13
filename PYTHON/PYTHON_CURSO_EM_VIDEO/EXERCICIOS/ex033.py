print('Digite os número abaixo para descobrir sua ordem:')
print()
num1 = int(input('1º número: '))
num2 = int(input('2º número: '))
num3 = int(input('3º número: '))
print()

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3
    
menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3
    
print('O maior valor é {}'.format(maior))
print('E o menor valor é {}'.format(menor))
