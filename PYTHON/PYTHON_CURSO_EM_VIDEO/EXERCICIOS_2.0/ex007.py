''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''

maior_idade = 0
homens = 0
mulheres_menos_20 = 0

while True:
    #ENTRADAS

    while True:

        age = input('Idade: ')
        try:
            val_age = int(age)
            break
        except ValueError:
            print('ERRO, digite um número inteiro')


    while True:

        gender = str(input('[M] ou [F]: ')).upper()
        if gender not in 'MF' or gender == '':
            print('ERRO')
        else:
            break


    # VALIDAÇÕES
    if val_age >= 18:
        maior_idade += 1
    if gender == 'M':
        homens += 1
    if val_age <= 20 and gender == 'F':
        mulheres_menos_20 += 1

    #VALIDAÇÃO DE SAÍDA
    print()
    keep = str(input('Continuar? [S/N]? ')).upper()
    if keep == 'N':
        print()
        break
    print()

print(f'MAIORES DE IDADE: {maior_idade}')
print(f'HOMENS: {homens}')
print(f'MULHERES COM MENOS DE 20 ANOS: {mulheres_menos_20}')
