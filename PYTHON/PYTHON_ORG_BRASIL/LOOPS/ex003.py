"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

while True:
    nome = str(input('Nome: '))
    if len(nome) < 3:
        print('O nome precisa ter no mínimo 3 caracteres.')
    else:
        break

while True:
    idade = int(input('Idade: '))
    if 0 < idade < 150:
        break
    else:
        print('A idade precisa ser menor que 150.')

while True:
    salario = float(input('Salário: R$'))
    if salario == 0:
        print('O salário precisa ser maior que R$0,00')
    else:
        break

while True:
    sexo = str(input('Sexo: '))
    if sexo not in 'MmFf':
        print('Digite M ou F')
    else:
        break

while True:
    print('Estado civil: S, C, V ou D')
    estado_civil = str(input(''))
    if estado_civil not in 'SCVD':
        print('Digite uma das opções. S, C, V ou D')
    else:
        break
