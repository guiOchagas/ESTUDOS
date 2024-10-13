dicio = {'nome': [], 'sexo': [], 'idade': []}
mulheres = []

while True:
    dicio['nome'].append(str(input('Nome: ')))
    dicio['sexo'].append(str(input('Sexo: [M/F] ' )))
    dicio['idade'].append(int(input('Idade: ')))
    print()
    continuar = str(input('Continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
    
print()
print(dicio)
print()

total_idade = 0

for c in dicio['idade']:
    total_idade += c

media_idade = total_idade / len(dicio['idade'])

for v in range(len(dicio['sexo'])):
    if dicio['sexo'][v] == 'F':
        mulheres.append(dicio['nome'][v][:])

acima_media = []

for v in range(len(dicio['idade'])):
    if dicio['idade'][v] > media_idade:
        acima_media.append(dicio['nome'][v])
        
print(acima_media)
    
    
    
print(f'- O grupo tem {len(dicio["nome"])} pessoas.')
print(f'- A média da idade é {media_idade:.2f} anos.')
print(f'- As mulheres cadastradas foram {mulheres}.')
print(f'- A lista das pessoas que estão acima da média:')

for v in range(len(dicio['idade'])):
    if dicio['idade'][v] > media_idade:
        print(f'NOME = {dicio["nome"][v]}; IDADE = {dicio["idade"][v]}', end=' ')
print()

