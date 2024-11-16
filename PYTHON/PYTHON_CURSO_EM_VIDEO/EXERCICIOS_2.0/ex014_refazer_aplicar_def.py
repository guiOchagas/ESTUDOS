"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

"""from random import randint


user = int(input('Quantos jogos você quer gerar? '))


lista_num = []

while len(lista_num) < 5:
    n = randint(1, 10)
    if n not in lista_num:
        lista_num.append(n)

print(lista_num)


print()
print('JOGOS SUGERIDOS')
for x in lista_num:
    print(f'   {x}   ', end='')"""


from random import randint

# Solicita ao usuário quantos jogos ele deseja gerar
user = int(input('Quantos jogos você quer gerar? '))

# Função para gerar um único jogo com 5 números únicos
def gerar_jogo():
    lista_num = []
    while len(lista_num) < 5:
        n = randint(1, 10)
        if n not in lista_num:
            lista_num.append(n)
    return lista_num

# Gera os jogos conforme a quantidade desejada
jogos = []
for _ in range(user):
    jogos.append(gerar_jogo())

# Exibe os jogos gerados
print()
print('JOGOS SUGERIDOS')
for jogo in jogos:
    print(f'{"   ".join(map(str, jogo))}')
