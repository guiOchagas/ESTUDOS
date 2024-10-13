from time import sleep
speed = int(input('Por favor, digite a velocidade do veículo: '))
multa = int(speed - 80) * 7
print()
print('PROCESSANDO...')
print()
sleep(2)
if speed > 80:
    print('MULTADO...')
    print('')
    print('O valor da multa é de R${:.2f}'.format(multa))
else:
    print('Você não foi multado!')
    print('Pode seguir, boa viagem!!!')
