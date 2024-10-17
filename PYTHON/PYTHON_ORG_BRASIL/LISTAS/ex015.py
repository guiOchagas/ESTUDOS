"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""

lista = []
nota = 0

print('[ DIGITE "-1" QUANDO FINALIZAR ]')

while True:
    nota = int(input('Digite uma nota: '))
    if nota >= 0:
        lista.append(nota)
    if nota == -1:
        break

print("Mostre a quantidade de valores que foram lidos;")
print(len(lista))
print()

print("Exiba todos os valores na ordem em que foram informados, um ao lado do outro;")
for nota in lista:
    print(nota, end=' ')
print()
print()

print("Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;")
lista.sort(reverse=True)
for nota in lista:
    print(nota)
print()

print("Calcule e mostre a soma dos valores;")
print(sum(lista))
print()

print("Calcule e mostre a média dos valores;")
media = (sum(lista) / len(lista))
print(media)
print()

print("Calcule e mostre a quantidade de valores acima da média calculada;")
for nota in lista:
    if nota > media:
        print(nota, end=' ')
print()
print()

print("Calcule e mostre a quantidade de valores abaixo de sete;")
lista.sort()
for nota in lista:
    if nota < 7:
        print(nota, end=' ')
print()
print()

print("Encerre o programa com uma mensagem;")
print('FIM DO PROGRAMA!')
