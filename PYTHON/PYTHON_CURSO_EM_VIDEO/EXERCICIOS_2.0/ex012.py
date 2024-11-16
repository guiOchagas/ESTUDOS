'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

cont = 0
lista = []
qtd = int(input('Deseja inserir quantos números? \n'))

for x in range(qtd):
    user = int(input('Digite: '))
    cont += 1

    #Validação de inserção na lista:
    if len(lista) == 0:
        lista.append(user)
        print(lista)
        print(f'[{user}] adicionado a lista.')
    else:
        if user > lista[-1]:
            lista.append(user)
            print(lista)
            print(f'[{user}] adicionado a posição [{(len(lista) - 1) + 1}]')
            

        elif user < lista[0]:
            lista.insert(0, user)
            print(lista)
            print(f'[{user}] adicionado a posição [{(lista.index(user)) + 1}]')
        
        #Validação para incluir o número digitado no meio da lista.
        else:
            for num in range(len(lista) - 1):
                if lista[num] < user < lista[num + 1]:
                    lista.insert(num + 1, user)
                    print(lista)
                    print(f'[{user}] adicionado a posição [{(lista.index(lista[num + 1])) + 1}]')
                    break

print(lista)


