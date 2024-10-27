lista_num = ['um', 'dois', 'tres', 'quatro', 'cinco']

user = int(input('Digite um número de 1 à 5: '))

num_ext = lista_num[user - 1]

print(f'Você digitou {user} = {num_ext.capitalize()}')
