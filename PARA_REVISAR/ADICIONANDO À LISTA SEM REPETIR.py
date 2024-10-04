lista = []
valor = True

while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    if valor in lista:
        print('Esse valor já foi adicionado.')
    else:
        lista.append(valor)
print(lista)
