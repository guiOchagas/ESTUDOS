casa = float(input('Digite o valor do imóvel: R$'))
tempo = int(input('Deseja pagar em quantos anos?: '))
salario = float(input('Digite o seu salário: R$'))
parcela = casa / (tempo * 12)
print()
print('O valor da sua parcela por mês é R${:.2f}.'.format(parcela))
print()
if parcela < 0.3 * salario:
    print('PARABÉNS! Seu financiamento foi aprovado e o valor da sua parcela por mês é R${:.2f}'.format(parcela))
else:
    print('NÃO APROVADO! Tente novamente.')
