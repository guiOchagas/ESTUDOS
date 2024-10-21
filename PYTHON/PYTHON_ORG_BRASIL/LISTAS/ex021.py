"""Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível.

Calcule e mostre:
O modelo do carro mais econômico;

Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro."""

carros = ['FOX', 'BMW', 'AUDI', 'PORSHE', 'FERRARI']
km_por_litro = [15, 8, 9, 5, 2]

lista_completa = dict(zip(carros, km_por_litro))
carro_mais_eficiente = max(lista_completa, key=lista_completa.get)


print(f'O modelo mais econômico é o {carro_mais_eficiente} com {lista_completa[carro_mais_eficiente]} km/l.')
