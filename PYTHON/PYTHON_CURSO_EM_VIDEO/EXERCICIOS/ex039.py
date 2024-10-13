from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
print()
if idade < 18:
    print('Você tem {} anos. Faltam {} anos para você se alistar.'.format(idade, 18 - idade))
elif idade == 18:
    print('URGENTE! Procure o posto mais próximo para você se alistar.')
else:
    print('Você tem {} anos, já se passaram {} do seu prazo de alistamento.'.format(idade, idade - 18))
