"""
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:

a: quantas pessoas foram cadastradas.
b: uma listagem com as pessoas mais pesadas
c: uma listagem com as pessoas mais leves

Obs.: Gerar uma lista com os mais leves e mais pesados
Vai depender de analisar qual é o mais leve e o mais pesado.
Se houver mais de um com esse peso, insere na lista.
O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
que é o motivo pelo qual a lista existe.

"""

soma_peso = 0
media_peso = 0
pessoas_cadastradas = 0

lista_leves = []
lista_pesadas = []
lista_geral = []

print('[0] para SAIR')


while True:
    #Input dos valores
    nome = str(input('Nome: '))
    if nome == '0':
        break
    peso = float(input('Peso: '))
    if peso == 0:
        break

    #Lista auxiliar para separar os dados das pessoas
    lista_auxiliar = []
    lista_auxiliar.append(nome)
    lista_auxiliar.append(peso)

    #Cópia da lista auxiliar para a lista geral.
    lista_geral.append(lista_auxiliar)

    #Média do peso das pessoas
    soma_peso += peso
    media = soma_peso / len(lista_geral)

    #Pessoas pesadas
    if peso > media:
        lista_pesadas.append(lista_auxiliar)
    
    #Pessoas leves
    if peso < media:
        lista_leves.append(lista_auxiliar)


print(lista_geral)
print(lista_pesadas)
print(lista_leves)

#Vizualiar lista geral
print('TODAS AS PESSOAS CADASTRADAS')
print('=' * 10)
for elemento in lista_geral:
    print()
    print(f'NOME: {elemento[0]}')
    print(f'PESO: {elemento[1]}')


#Vizualiar lista das pessoas mais pesadas
print('LISTA DAS PESSOAS MAIS PESADAS')
print('=' * 10)
for elemento in lista_pesadas:
    print()
    print(f'NOME: {elemento[0]}')
    print(f'PESO: {elemento[1]}')

#Vizualiar lista das pessoas mais leves
print('LISTA DAS PESSOAS MAIS PESADAS')
print('=' * 10)
for elemento in lista_leves:
    print()
    print(f'NOME: {elemento[0]}')
    print(f'PESO: {elemento[1]}')
