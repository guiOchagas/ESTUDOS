'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''

sexo = str(input('Sexo: ')).upper()

while sexo not in 'MF':
    print('Digite apenas [M] ou [F]')
    sexo = str(input('Sexo: ')).upper()
    
print(sexo)
