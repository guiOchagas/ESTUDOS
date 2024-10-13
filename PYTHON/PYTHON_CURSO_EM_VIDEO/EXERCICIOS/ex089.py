lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    print()
    
    lista.append([nome, [nota1, nota2], media])
    
    resp = str(input('Continuar? [S/N] '))
    print()
    if resp in 'Nn':
        break

print('=' * 30)
print(f'{"Nº":<5}{"NOME":<20}{"MÉDIA":>5}')
print('=' * 30)
for i, p in enumerate(lista):
    print(f'{i:<5}{p[0]:<20}{p[2]:>5.1f}')

while True:
    print()
    print('=' * 30)
    
    opcao = int(input('Digite o nº do aluno para ver as notas (999 finaliza): '))
    print()
    
    if opcao <= len(lista) - 1:
        print(f'As notas de {lista[opcao][0]} foram {lista[opcao][1]}\nPor isso ele(a) ficou com a média {lista[opcao][2]}')
        
    if opcao == 999:
        print('FUI...')
        break
