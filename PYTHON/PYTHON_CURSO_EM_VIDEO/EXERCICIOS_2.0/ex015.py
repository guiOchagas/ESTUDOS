"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""
from datetime import date

trabalho = {}


today = date.today().year

nome = str(input('NOME: '))
nasc = int(input('ANO DE NASCIMENTO: '))
ctps = int(input('CTPS: '))

trabalho['NOME'] = nome
trabalho['NASC'] = today - nasc
trabalho['CTPS'] = ctps

if ctps != 0:
    contrato = int(input('ANO DE CONTRAÇÃO: '))
    salario = float(input('SALÁRIO: '))
    trabalho['CONTRATO'] = contrato
    trabalho['SALÁRIO'] = salario



for chave, valor in trabalho.items():
    print(f'{chave:<10}: {valor}')
