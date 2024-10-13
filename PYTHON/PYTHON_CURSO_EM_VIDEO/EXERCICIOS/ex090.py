escola = {}
escola['aluno'] = str(input('Aluno: '))
escola['media'] = int(input('Média: '))
print()

if escola['media'] >= 7:
    escola['situação'] = 'Aprovado'
elif escola['media'] >= 5 and escola['media'] <= 7:
    escola['situação'] = 'Recuperação'
else:
    escola['situação'] = 'Reprovado'

for k, v in escola.items():
    print(f'O {k} é igual a {v}')
