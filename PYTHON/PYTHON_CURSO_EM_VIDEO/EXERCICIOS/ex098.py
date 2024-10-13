from time import sleep

def contador(i, f, p):
    
    if p == 0:
        p = 1
        
    if p < 0:
        p *= -1
        
    if i <= f:
        print(f'Contando de {i} à {f}...')
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            cont += p
            sleep(0.1)
            
    if i >= f:
        print(f'Contando de {i} à {f}...')
        while i >= f:
            print(f'{i}', end=' ', flush=True)
            i -= p
            sleep(0.1)
            
contador(1, 10, 1)
print()
print()

contador(10, 1, 1)
print()
print()

print("Now, it's your turn!")

resp = 'S'

while resp != 'N':
    inicio = int(input(f'{"Inicio:":<10}'))
    fim = int(input(f'{"Fim:":<10}'))
    passo = int(input(f'{"Passo:":<10}'))
    
    contador(inicio, fim, passo)
    print()
    print()
    
    resp = str(input('Continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print()
print('FIM')
print('VOCÊ VAI SE TORNAR UM HOMEM DE MUITO SUCESSO! PARABÉNS...')
