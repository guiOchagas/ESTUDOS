nota = 0

while True:
    try:
        nota = int(input('Digite um número: '))
        print(f'Você digitou o número {nota}')
        break
    except:
        print('Você digitou um valor inválido, por favor digite um número inteiro.')
