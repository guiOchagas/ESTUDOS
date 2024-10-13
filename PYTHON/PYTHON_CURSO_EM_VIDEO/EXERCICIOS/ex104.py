def leiaInt():
    ok = False
    valor = 0
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break
        else:
            print('ERRO.')
    return valor

n = leiaInt()
print(f'Você acabou de digitar {n}.')
