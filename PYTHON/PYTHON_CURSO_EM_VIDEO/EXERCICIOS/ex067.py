from time import sleep
while True:
    print('-'*35)
    print(' Quer ver a tabuada de qual valor?')
    print('-'*35)
    print()
    num = int(input(''))
    sleep(1)
    print()
    if num == 0:
        break
    for c in range (1,11):
        soma = num * c
        print(f'{num} x {c} = {soma}')
    print()
print('FINALIZANDO...')
sleep(2)
