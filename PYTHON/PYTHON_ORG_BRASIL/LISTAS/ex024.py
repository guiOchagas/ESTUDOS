"""Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados."""

from random import randint

lista = []

for valor in range(10):
    lista.append(randint(1, 10))
    
print(lista)

contagem = {}

for valor in lista:
    if valor in contagem:
        contagem[valor] += 1
    else:
        contagem[valor] = 1

print()
print()

print("Contagem de valores:")
for valor, quantidade in contagem.items():
    print(f"{valor}: {quantidade}")
    
