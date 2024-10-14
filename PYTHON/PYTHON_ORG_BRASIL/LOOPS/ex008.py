"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

lista = []

for c in range(5):
    num = int(input(f"Número {c+1}: "))
    lista.append(num)

print(f"A soma dos números é {sum(lista)} e a média é {sum(lista) / len(lista)}.")
