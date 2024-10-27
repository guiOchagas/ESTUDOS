"""Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas."""


def inverter_string(string):
    texto_invertido = ''.join(reversed(string))
    return texto_invertido.upper()

nome = str(input('Digite seu nome: '))

invertido = inverter_string(nome)
print(invertido)
