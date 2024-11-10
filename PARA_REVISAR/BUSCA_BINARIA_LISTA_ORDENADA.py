lista = [4, 6, 2, 7, 3, 8, 1, 9]
lista.sort()  # A lista deve estar ordenada para a busca binária funcionar corretamente.

#lista ordenada = [1, 2, 3, 4, 6, 7, 8, 9]

target = 1
i = 0
f = len(lista) - 1
cont = 0

while i <= f:
    meio = (i + f) // 2  # Calcula o índice do meio
    cont += 1
    
    if lista[meio] == target:  # Encontrou o alvo
        print(f'Valor encontrado com {cont} tentativa(s)')
        break
    elif lista[meio] < target:  # Se o valor no meio for menor que o alvo, busque na metade direita
        i = meio + 1
    else:  # Se o valor no meio for maior que o alvo, busque na metade esquerda
        f = meio - 1
else:
    print(f'Valor {target} não encontrado após {cont} tentativa(s)')

print('FIM')
