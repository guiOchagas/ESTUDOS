print('=' * 25)
print(' CALCULADORA DE AUMENTO')
print('=' * 25)
print()
salario = float(input('Digite seu salario: R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} agora estará ganhando R${:.2f}'.format(salario, novo))
