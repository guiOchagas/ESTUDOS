print('='*20)
print('  Cálucle seu IMC')
print('='*20)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura ** 2)
print()
print('Seu IMC é: {:.2f}'.format(IMC))
print()
print('Sua categoria é:')
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC > 18.5 and IMC < 25:
    print('PESO IDEAL')
elif IMC > 25 and IMC < 30:
    print('SOBREPESO')
elif IMC > 30 and IMC < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
