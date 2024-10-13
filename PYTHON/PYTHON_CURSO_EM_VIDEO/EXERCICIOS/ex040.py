n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print()
print('A nota final é {:.1f}'.format((n1 + n2) / 2))
if (n1 + n2) / 2 < 5:
    print('REPROVADO')
elif (n1 + n2) / 2 > 5 and (n1 + n2) / 2 < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
