from random import randint

def sorteio(lista):
  for c in range(5):
    lista.append(randint(0,9))
  print(numeros)

def somaPar(lista):
  somapar = 0
  for c in lista:
    if c % 2 == 0:
      somapar += c
  print(f'A soma dos números pares é {somapar}')

def somaImpar(lista):
  somaimpar = 0
  for c in lista:
    if c % 2 == 1:
      somaimpar += c
  print(f'A soma dos valores impares é {somaimpar}')      

numeros = []
sorteio(numeros)
print()
somaPar(numeros)
somaImpar(numeros)
