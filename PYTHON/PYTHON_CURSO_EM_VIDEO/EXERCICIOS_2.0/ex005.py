''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''

flag = True
cont = 0
soma = 0

while flag:
    user = int(input('Digite um número: '))
    
    cont += 1
    soma += user
    
    while True:
        
        keep = str(input('Continuar? [S/N]:\n')).upper()
        
        if keep == 'S':
            break
        
        elif keep == 'N':
            flag = False
            break
        
        else:
            print('ERRO')
    
    
media = soma / cont
print(f'SOMA: {soma}\nMÉDIA: {media}\nENTRADAS: {cont}')
