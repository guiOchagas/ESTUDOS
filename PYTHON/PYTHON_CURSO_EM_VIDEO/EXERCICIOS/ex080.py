lista = []
for c in range(0, 5):
    r = int(input('Digite um valor: '))
    if c == 0 or r > lista[-1]:
        lista.append(r)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if r <= lista[pos]:
                lista.insert(pos, r)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('='*30)
print(lista)
