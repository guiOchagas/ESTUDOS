from time import sleep
num = ('um', 'dois', 'três', 'quatro', 'cinco')
while True:
    dig = int(input('Digite um número de [1] à [5], ou [0] para sair. '))
    if dig >= 1 and dig <= 5:
        print(f'O número [{dig}] por extenso é {num[dig-1].upper()}')
        print()
    elif dig == 0:
        print('Encerrando...')
        sleep(2)
        print('Até a próxima!')
        break
    else:
        print('Opção inválida.')
        print()
