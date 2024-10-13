count = num = soma = 0
num = int(input('Digite um número, [999 p/ sair]: '))
while num != 999:
    count += +1
    soma += num
    num = int(input('Digite um número, [999 p/ sair]: '))
print()
print(f'Você digitou {count} números e a soma entre eles é {soma}')
