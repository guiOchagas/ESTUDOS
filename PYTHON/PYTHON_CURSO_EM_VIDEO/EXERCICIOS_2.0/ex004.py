'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)

'''

user = int(input('Digite um número: '))
n1 = n2 = 1
cont = 0

"""for x in range(user):
    print(n1, end='  ')
    
    print(n2, end='  ')
    
    n1 += n2 # 2 - 5 - 13 
    
    n2 += n1 # 3 - 8 - 21"""
    
while cont != user:
    cont += 1
    
    print(n1, end='  ')
    
    print(n2, end='  ')
    
    n1 += n2 # 2 - 5 - 13 
    
    n2 += n1 # 3 - 8 - 21
