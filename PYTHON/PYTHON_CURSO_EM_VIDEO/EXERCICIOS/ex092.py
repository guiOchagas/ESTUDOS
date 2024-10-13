from datetime import date
hoje = date.today().year

dicio = {'Nome': {}, 'Idade': {}, 'CTPS': {}, 'Contratação': {}, 'Salário': {}, 'Aposentadoria': {}}
c = 0

while True:
    dicio['Nome'] = str(input('Nome: '))
    
    while True:
        ano_nascimento = int(input('Ano de nascimento: '))
        if ano_nascimento > hoje:
            print(f'Você veio do futuro?')
        else:
            break
    dicio['Idade'] = hoje - ano_nascimento
    
    
    dicio['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
    if dicio['CTPS'] == 0:
        break
    dicio['Contratação'] = int(input('Ano de contratação: '))
    dicio['Salário'] = int(input('Salário: R$'))
    
    continuar = str(input('Continuar? [S/N] ')).lower().strip()
    if continuar != 's':
        break

dicio['Aposentadoria'] = dicio['Contratação'] + 35 - hoje + dicio['Idade']

print()
print('='*20)
print()
print(dicio)
print()
for k, v in dicio.items():
    print(f'{k} tem o valor [ {v} ]')
    
print()
print('='*20)
print()

print(f'Seu nome é {dicio["Nome"]}.')
print(f'Você tem {dicio["Idade"]}.')
print(f'CTPS número: {dicio["CTPS"]}.')
print(f'Ano de contratação: {dicio["Contratação"]}.')
print(f'Salário: R${dicio["Salário"]}.')
print(f'Vai se aposentar com: {dicio["Aposentadoria"]} anos.')


    
