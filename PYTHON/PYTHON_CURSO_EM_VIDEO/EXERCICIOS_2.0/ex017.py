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


pessoas = {'NOMES': list(), 'IDADES': list(), 'GENERO': list()}


while True:
    nome = str(input('NOME: ')).capitalize()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: ')).upper()[0]

    pessoas['NOMES'].append(nome)
    pessoas['IDADES'].append(idade)
    pessoas['GENERO'].append(sexo)

    continuar = str(input('Continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

#Total de pessoas cadastradas
print(pessoas)
print(f'Total de pessoas cadastradas: {len(pessoas['NOMES'])}')

#Idade média do grupo
media = sum(pessoas['IDADES']) / len(pessoas['IDADES'])
print(f'Média de idade: {media}')

#Mulheres cadastradas
for pessoa in pessoas['GENERO']:
    if pessoa == 'F':
        print(pessoas['NOMES'])
