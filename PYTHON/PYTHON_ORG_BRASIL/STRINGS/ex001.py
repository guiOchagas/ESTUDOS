"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente."""

def validador(s1, s2):
    print(f'String 1: {s1}')
    print(f'String 2: {s2}')
    print(f'Tamanho de "{s1}": {len(s1)}')
    print(f'Tamanho de "{s2}": {len(s2)}')
    
    #VERIFICAÇÃO DE TAMANHO
    if len(s1) == len(s2):
        print('As duas strings são de tamanhos iguais.')
    else:
        print('As duas strings são de tamanhos diferentes.')
    
    #VERIFICAÇÃO DE CONTEUDO
    if s1 == s2:
        print(f'As duas strings possuem o mesmo conteúdo.')
    else:
        print(f'As duas strings possuem conteúdos diferentes.')
    
str1 = str(input('DIGITE A 1 FRASE: '))
str2 = str(input('DIGITE A 2 FRASE: '))

result = validador(str1, str2)
print(result)

