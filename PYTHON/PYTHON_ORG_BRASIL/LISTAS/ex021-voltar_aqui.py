"""Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível.

Calcule e mostre:
O modelo do carro mais econômico;

Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43"""

carros = ['FOX', 'BMW', 'AUDI', 'PORSHE', 'FERRARI']
km_por_litro = [15, 8, 9, 5, 2]
gasolina = 2.25

lista_completa = dict(zip(carros, km_por_litro))
carro_mais_eficiente = max(lista_completa, key=lista_completa.get)


print(f'O modelo mais econômico é o {carro_mais_eficiente} com {lista_completa[carro_mais_eficiente]} km/l.')

print(f'Considerando que iremos fazer uma viagem de 1000 quilômetros e o preço da gasolina é R${gasolina}.')

print('RELATÓRIO FINAL')

for i, (carro, km) in enumerate(lista_completa.items()):
    total = (1000 / km) * gasolina
    print(f'{i + 1} - {carro:<10} - {km:<3} km/h - {1000 / km:<6.2f} litros - {total:<5.2f}')
    

