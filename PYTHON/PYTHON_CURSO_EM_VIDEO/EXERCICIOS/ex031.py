from time import sleep
distancia = int(input('Qual foi a distância da viagem em metros? '))
print()
print('PROCESSANDO...')
sleep(3)
print()
print('O tamanho da sua viagem foi de {} metros'.format(distancia))
if distancia <= 200:
    print('e o preço ficou um total de: R${:.2f}'.format(distancia * 0.5))
else:
    print('e o preço ficou um total de: R${:.2f}'.format(distancia * 0.45))
