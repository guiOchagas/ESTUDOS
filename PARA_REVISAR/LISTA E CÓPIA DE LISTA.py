lista = []
temp = []
qtd = 0
pesado = 100
leve = 60

print('Digite [0] quando terminar.')

while True:
    nome = str(input('Nome: '))
    if nome == '0':
        break
    peso = float(input('Peso: '))
    if peso == 0:
        break
    qtd += 1
    temp.append(nome)
    temp.append(peso)
    lista.append(temp[:])
    temp.clear()

print(lista)

print(f'LISTA DOS MAIS PESADOS: ')

for e in lista:
    if e[1] > pesado:
        print(f'{e[0]}')

print(f'LISTA DOS MAIS LEVES: ')

for e in lista:
    if e[1] < leve:
        print(f'{e[0]}')
