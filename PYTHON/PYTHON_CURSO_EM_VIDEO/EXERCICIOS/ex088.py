from random import randint
lista = []
jogos = []
cont  = 0
resp = int(input('Quantos jogos você quer? '))
while total <= resp:
    while True:
        num = randint(1, 100)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
        jogos.append(lista[:])
        lista.clear()
        total += 1
    
print(jogos)
