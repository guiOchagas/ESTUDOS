def linha(msg):
    print('='*30)
    print(msg)
    print('='*30)
    
def calc(l, c):
    area = l * c
    print(f'A área de um terreno {l} x {c} é de {area:.2f}m²')
    
    
linha(f'{"CONTROLE DE TERRENOS":-^30}')

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print()
calc(l, c)
print()
linha(f'{"FIM":-^30}')
