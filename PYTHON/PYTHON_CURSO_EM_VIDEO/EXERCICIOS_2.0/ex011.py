'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = []
cont = 0
flag = True

while True:
    digite = int(input('Digite: '))
    if digite == 0:
        break
    if digite not in lista:
        lista.append(digite)
        cont += 1
    elif digite in lista:
        print('Valor já adicionado.')
    
print(lista)
