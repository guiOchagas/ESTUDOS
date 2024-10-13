lista = []
dados = []
lista_pesado = []
lista_leve = []

for c in range(2):
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    cont += 1

for v in lista:
    if v[1] >= 100:
        lista_pesado.append(v)

for v in lista:
    if v[1] <= 60:
        lista_leve.append(v)


print()
print(lista)
print()
print(f'Foram cadastradas {len(lista)} pessoas')
print()
print(lista_pesado)
print()
print(lista_leve)
