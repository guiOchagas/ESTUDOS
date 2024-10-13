lista = []

def maior(* num):
  maior = 0
  for n in num:
    if maior < n:
      maior = n

  print()
  print(f'O maior valor é {maior}')
  print()
  print(f'Os número digitados foram {num} e o maior é o {maior}')
  
for c in range(3):
  numeros = int(input('Digite um número: '))
  lista.append(numeros)  # Adiciona os números à lista
  
maior(*lista)
