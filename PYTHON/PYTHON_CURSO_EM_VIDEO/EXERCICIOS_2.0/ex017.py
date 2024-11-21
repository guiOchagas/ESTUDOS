"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""


pessoa = {}
geral = []

soma_idade = 0
media_idade = 0


while True:

    pessoa.clear()

    nome = str(input('NOME: ')).capitalize()
    idade = int(input('IDADE: '))
    soma_idade += idade

    #Validação
    while True:
        sexo = str(input('SEXO: ')).upper()[0]
        if sexo in 'MF':
            break
        else:
            print('Erro, digite apenas [M] ou [F]')

    pessoa['NOME'] = nome
    pessoa['IDADE'] = idade
    pessoa['GENERO'] = sexo

    geral.append(pessoa.copy())

    print()
    continuar = str(input('Continuar? [S/N] ')).upper()
    print()
    if continuar == 'N':
        break


print(pessoa)
print(geral)

print()

# Quantidade de pessoas cadastradas
print(f'TOTAL DE PESSOAS CADASTRADAS: {len(geral)}')
print()

# Média de idade do grupo
media_idade = soma_idade / len(geral)
print(f'MÉDIA DE IDADE DO GRUPO: {media_idade}')
print()

# Mulheres cadastradas
print('LISTA DE MULHERES CADASTRADAS:')
for x in geral:
    if x['GENERO'] == 'F':
        print(f"• {x['NOME']}")
print()
    
# Lista com as pessoas com idade acima da média
print('LISTA DAS PESSOAS COM IDADE ACIMA DA MÉDIA:')
for x in geral:
    if x['IDADE'] > media_idade:
        print(f"• {x['NOME']}")
print()
